(function(){
  var canvas = document.getElementById('bg-canvas');
  var cursorDot = document.getElementById('cursor-dot');
  if (!canvas || !cursorDot) return;

  var ctx = canvas.getContext('2d');
  var w = window.innerWidth;
  var docH = window.innerHeight;
  var dpr = Math.min(window.devicePixelRatio || 1, 2);
  var nodes = [];
  var mouse = { x: null, y: null, active: false };
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function makeNode(){
    return {
      x: Math.random() * w,
      y: Math.random() * docH,
      vx: (Math.random() - .5) * .3,
      vy: (Math.random() - .5) * .3,
      z: .35 + Math.random() * .65
    };
  }

  function resize(){
    w = window.innerWidth;
    var newDocH = Math.max(document.documentElement.scrollHeight, document.body.scrollHeight, window.innerHeight);
    var grew = newDocH > docH;
    docH = newDocH;

    canvas.width = w * dpr;
    canvas.height = window.innerHeight * dpr;
    canvas.style.width = w + 'px';
    canvas.style.height = window.innerHeight + 'px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    var count = reduceMotion ? 70 : Math.max(120, Math.min(320, Math.round((w * docH) / 7600)));
    if (!nodes.length){
      nodes = [];
      for (var i = 0; i < count; i += 1) nodes.push(makeNode());
    } else if (grew){
      while (nodes.length < count) nodes.push(makeNode());
    } else if (nodes.length > count){
      nodes.length = count;
    }
  }

  function step(){
    var vh = window.innerHeight;
    var scrollY = window.scrollY;
    var mx = mouse.active ? mouse.x : null;
    var my = mouse.active ? mouse.y : null;
    ctx.clearRect(0, 0, window.innerWidth, vh);

    for (var i = 0; i < nodes.length; i += 1){
      var n = nodes[i];
      if (!reduceMotion){
        n.x += n.vx;
        n.y += n.vy;
        if (n.x < 0){ n.x = 0; n.vx *= -1; }
        if (n.x > w){ n.x = w; n.vx *= -1; }
        if (n.y < 0){ n.y = 0; n.vy *= -1; }
        if (n.y > docH){ n.y = docH; n.vy *= -1; }

        n.vx += (Math.random() - .5) * .006;
        n.vy += (Math.random() - .5) * .006;
        var speed = Math.sqrt(n.vx * n.vx + n.vy * n.vy);
        if (speed > .45){
          n.vx = n.vx / speed * .45;
          n.vy = n.vy / speed * .45;
        }
      }

      if (mx !== null){
        var dx = n.x - mx;
        var dy = (n.y - scrollY) - my;
        var d = Math.sqrt(dx * dx + dy * dy);
        if (d < 160 && d > .01){
          var f = (160 - d) / 160 * .05;
          n.vx += dx / d * f;
          n.vy += dy / d * f;
        }
      }
    }

    var buffer = 60;
    for (var aIdx = 0; aIdx < nodes.length; aIdx += 1){
      var a = nodes[aIdx];
      var ay = a.y - scrollY;
      if (ay < -buffer || ay > vh + buffer) continue;

      for (var bIdx = aIdx + 1; bIdx < nodes.length; bIdx += 1){
        var b = nodes[bIdx];
        var by = b.y - scrollY;
        if (by < -buffer || by > vh + buffer) continue;
        var ldx = a.x - b.x;
        var ldy = ay - by;
        var dist = Math.sqrt(ldx * ldx + ldy * ldy);
        if (dist < 140){
          ctx.strokeStyle = 'rgba(37,84,232,' + ((1 - dist / 140) * .10 * ((a.z + b.z) / 2)) + ')';
          ctx.lineWidth = 1;
          ctx.beginPath();
          ctx.moveTo(a.x, ay);
          ctx.lineTo(b.x, by);
          ctx.stroke();
        }
      }

      var glow = 0;
      if (mx !== null){
        var cdx = a.x - mx;
        var cdy = ay - my;
        var cdist = Math.sqrt(cdx * cdx + cdy * cdy);
        if (cdist < 200) glow = 1 - cdist / 200;
      }
      ctx.beginPath();
      ctx.arc(a.x, ay, (1.4 * a.z + .6) + glow * 2.6, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(37,84,232,' + Math.min(1, (.18 * a.z + .06) + glow * .75) + ')';
      ctx.fill();
    }

    if (mx !== null){
      for (var i = 0; i < nodes.length; i += 1){
        var cn = nodes[i];
        var cy = cn.y - scrollY;
        var ddx = cn.x - mx;
        var ddy = cy - my;
        var cd = Math.sqrt(ddx * ddx + ddy * ddy);
        if (cd < 190){
          ctx.strokeStyle = 'rgba(37,84,232,' + ((1 - cd / 190) * .55) + ')';
          ctx.lineWidth = 1.1;
          ctx.beginPath();
          ctx.moveTo(mx, my);
          ctx.lineTo(cn.x, cy);
          ctx.stroke();
        }
      }
    }

    requestAnimationFrame(step);
  }

  window.addEventListener('mousemove', function(e){
    mouse.x = e.clientX;
    mouse.y = e.clientY;
    mouse.active = true;
    cursorDot.style.left = e.clientX + 'px';
    cursorDot.style.top = e.clientY + 'px';
  }, { passive: true });
  window.addEventListener('mouseleave', function(){ mouse.active = false; });
  window.addEventListener('mousedown', function(e){
    var ripple = document.createElement('span');
    ripple.className = 'cursor-ripple';
    ripple.style.left = e.clientX + 'px';
    ripple.style.top = e.clientY + 'px';
    document.body.appendChild(ripple);
    ripple.addEventListener('animationend', function(){ ripple.remove(); });
    cursorDot.style.transform = 'translate(-50%,-50%) scale(.6)';
  });
  window.addEventListener('mouseup', function(){
    cursorDot.style.transform = 'translate(-50%,-50%) scale(1)';
  });

  resize();
  step();
  window.addEventListener('load', resize);
  window.addEventListener('resize', resize);
  if (window.ResizeObserver) new ResizeObserver(resize).observe(document.body);

  var navLinks = Array.prototype.slice.call(document.querySelectorAll('.side-nav a[href^="#"]'));
  var sections = navLinks.map(function(a){ return document.querySelector(a.getAttribute('href')); });
  function setActiveSection(){
    var pos = window.scrollY + 140;
    var activeId = sections[0] ? sections[0].id : '';
    sections.forEach(function(section){
      if (section && section.offsetTop <= pos) activeId = section.id;
    });
    navLinks.forEach(function(link){
      link.classList.toggle('active', link.getAttribute('href') === '#' + activeId);
    });
  }
  setActiveSection();
  window.addEventListener('scroll', setActiveSection, { passive: true });
})();
