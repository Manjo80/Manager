(function(){
  function ensureWrapped(img){
    if(img.closest(".marker-wrap")) return img.closest(".marker-wrap");
    const wrap = document.createElement("div");
    wrap.className = "marker-wrap";
    img.parentNode.insertBefore(wrap, img);
    wrap.appendChild(img);
    return wrap;
  }

  function parseMarkers(img){
    const raw = img.dataset.markers;
    if(!raw) return [];
    try { return JSON.parse(raw) || []; } catch(e){ return []; }
  }

  function sortedMarkers(markers){
    return markers.slice().sort((a,b)=>{
      const oa = (a.order ?? a.id ?? 0);
      const ob = (b.order ?? b.id ?? 0);
      return oa - ob;
    });
  }

  function asFloat(v, fallback=0){
    const n = Number(v);
    return Number.isFinite(n) ? n : fallback;
  }

  function normalize01(v){
    // Expected: already 0..1. If someone stored 0..100, convert.
    v = asFloat(v, 0);
    if(v > 1.0 && v <= 100.0) return v / 100.0;
    return v;
  }

  function markerCenter(marker){
    return { x: normalize01(marker.x), y: normalize01(marker.y) };
  }

  function buildSvgOverlay(wrap){
    const layer = document.createElement("div");
    layer.className = "marker-layer";

    const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    svg.setAttribute("class", "marker-svg");
    svg.setAttribute("viewBox", "0 0 1 1");
    svg.setAttribute("preserveAspectRatio", "none");

    layer.appendChild(svg);
    wrap.appendChild(layer);
    return { layer, svg };
  }

  function drawCircle(svg, x, y, r){
    const c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    c.setAttribute("class", "shape");
    c.setAttribute("cx", x);
    c.setAttribute("cy", y);
    c.setAttribute("r", r);
    svg.appendChild(c);
  }

  function drawRect(svg, x, y, w, h){
    const rect = document.createElementNS("http://www.w3.org/2000/svg", "rect");
    rect.setAttribute("class", "shape");
    rect.setAttribute("x", x - w/2);
    rect.setAttribute("y", y - h/2);
    rect.setAttribute("width", w);
    rect.setAttribute("height", h);
    svg.appendChild(rect);
  }

  function drawNumber(svg, x, y, n){
    // red circle background
    const bg = document.createElementNS("http://www.w3.org/2000/svg", "circle");
    bg.setAttribute("class", "num-bg");
    bg.setAttribute("cx", x);
    bg.setAttribute("cy", y);
    bg.setAttribute("r", 0.03);
    svg.appendChild(bg);

    const t = document.createElementNS("http://www.w3.org/2000/svg", "text");
    t.setAttribute("class", "num-text");
    t.setAttribute("x", x);
    t.setAttribute("y", y);
    t.setAttribute("font-size", "0.045");
    t.textContent = String(n);
    svg.appendChild(t);
  }

  function applyOverlayToImage(img, startNumber){
    if(img.dataset.markerOverlayApplied === "1") return startNumber;

    const markers = sortedMarkers(parseMarkers(img)).filter(m => (m.marker_type || m.type) !== "arrow");
    if(!markers.length){
      img.dataset.markerOverlayApplied = "1";
      return startNumber;
    }

    const wrap = ensureWrapped(img);
    const existing = wrap.querySelector(":scope > .marker-layer");
    if(existing) existing.remove();

    const { svg } = buildSvgOverlay(wrap);

    let next = startNumber;
    const photoId = img.dataset.photoId || img.getAttribute("data-photo-id") || null;

    markers.forEach(m=>{
      const mt = (m.marker_type || m.type || "circle");
      const {x,y} = markerCenter(m);

      if(mt === "rect"){
        const w = normalize01(m.w);
        const h = normalize01(m.h);
        drawRect(svg, x, y, w, h);
      }else{
        const r = normalize01(m.r || 0.05);
        drawCircle(svg, x, y, r);
      }

      drawNumber(svg, x, y, next);
      m.__num = next;
      next += 1;
    });

    // Fill note list under the photo (per photo)
    if(photoId){
      const list = document.querySelector(`ol.marker-notes[data-photo-id="${CSS.escape(photoId)}"]`);
      if(list){
        list.innerHTML = "";
        markers.forEach(m=>{
          const li = document.createElement("li");
          const note = (m.note ?? m.label ?? "").toString().trim();
          li.textContent = note ? `${m.__num}. ${note}` : `${m.__num}.`;
          list.appendChild(li);
        });
        if(!markers.length) list.innerHTML = "";
      }
    }

    img.dataset.markerOverlayApplied = "1";
    return next;
  }

  function applyAll(){
    // Ensure numbering is sequential across all photos on the detail page
    let n = 1;
    document.querySelectorAll("img[data-markers][data-photo-id]").forEach(img=>{
      n = applyOverlayToImage(img, n);
    });
  }

  // Run now and after dynamic DOM updates (modal enlarge inserts a new img)
  document.addEventListener("DOMContentLoaded", applyAll);
  window.addEventListener("load", applyAll);

  const mo = new MutationObserver((mutations)=>{
    for(const m of mutations){
      for(const node of m.addedNodes){
        if(!(node instanceof HTMLElement)) continue;
        if(node.matches && node.matches("img[data-markers][data-photo-id]")){
          applyAll();
          return;
        }
        const img = node.querySelector && node.querySelector("img[data-markers][data-photo-id]");
        if(img){ applyAll(); return; }
      }
    }
  });
  mo.observe(document.documentElement, {subtree:true, childList:true});

  // Export for manual use if needed
  window.MarkerOverlay = { applyAll };
})();
