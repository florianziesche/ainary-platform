// ============================================================================
// BINARY STAR CANVAS ANIMATION - EMBEDDABLE COMPONENT
// ============================================================================
// Professional-grade binary star animation for Ainary Ventures hero section.
// Quality-first: Realistic astrophysics, subtle aesthetics, optimized performance.
// 
// Usage:
// 1. Add canvas element: <canvas id="binary-star-bg"></canvas>
// 2. Include this script
// 3. Call: initBinaryStarAnimation('binary-star-bg')
// ============================================================================

function initBinaryStarAnimation(canvasId, config = {}) {
  const canvas = document.getElementById(canvasId);
  if (!canvas) {
    console.error(`Binary Star: Canvas element "${canvasId}" not found`);
    return null;
  }
  
  const ctx = canvas.getContext('2d', { alpha: true });
  
  let width, height, centerX, centerY;
  let animationId;
  let time = 0;
  
  // Performance scaling
  const isMobile = window.innerWidth < 768;
  const isHighPerf = !isMobile && window.devicePixelRatio <= 2;
  
  // ============================================================================
  // CONFIGURATION (with override support)
  // ============================================================================
  
  const CONFIG = {
    // Colors (brand-aligned)
    colorHuman: config.colorHuman || '#c8aa50',      // Gold - Human
    colorAI: config.colorAI || '#e8f0ff',            // Silver-white - AI
    colorStream: config.colorStream || '#ffffff',    // Particle streams
    
    // Orbital mechanics
    orbitScale: config.orbitScale || 0.22,
    orbitSpeed: config.orbitSpeed || 0.08,
    eccentricity: config.eccentricity || 0.15,
    
    // Star properties
    starRadius: {
      human: isMobile ? 8 : (config.starRadiusHuman || 12),
      ai: isMobile ? 7 : (config.starRadiusAI || 10)
    },
    glowRadius: {
      human: isMobile ? 60 : (config.glowRadiusHuman || 100),
      ai: isMobile ? 50 : (config.glowRadiusAI || 85)
    },
    
    // Particle systems (v2: drastically reduced — bridge is the hero, not particles)
    particles: {
      stream: isMobile ? 15 : (config.particlesStream || 30),
      orbit: isMobile ? 25 : (config.particlesOrbit || 50),
      ambient: isMobile ? 15 : (config.particlesAmbient || 30)
    },
    
    // Visual quality
    glowIntensity: config.glowIntensity || 0.15,
    trailFade: config.trailFade || 0.03,
    particleSpeed: config.particleSpeed || 0.4,
    
    // Performance
    pixelRatio: Math.min(window.devicePixelRatio, 2),
    
    // Background
    backgroundColor: config.backgroundColor || '#0a0a0b'
  };
  
  // ============================================================================
  // PARTICLE CLASS
  // ============================================================================
  
  class Particle {
    constructor(x, y, type) {
      this.x = x;
      this.y = y;
      this.type = type;
      this.life = 1;
      this.maxLife = 1;
      
      if (type === 'stream') {
        this.speed = 0.15 + Math.random() * 0.2;
        this.size = 0.4 + Math.random() * 0.6;
        this.color = CONFIG.colorStream;
        this.alpha = 0.1 + Math.random() * 0.15;
        this.angle = Math.random() * Math.PI * 2;
      } else if (type === 'orbit') {
        this.speed = 0.1 + Math.random() * 0.2;
        this.size = 0.5 + Math.random() * 0.8;
        this.alpha = 0.2 + Math.random() * 0.3;
        this.angle = Math.random() * Math.PI * 2;
        this.orbitRadius = Math.random() * 50 + 20;
      } else if (type === 'ambient') {
        this.x = Math.random() * width;
        this.y = Math.random() * height;
        this.size = 0.3 + Math.random() * 0.7;
        this.alpha = 0.1 + Math.random() * 0.2;
        this.twinkleSpeed = 0.01 + Math.random() * 0.02;
        this.twinklePhase = Math.random() * Math.PI * 2;
      }
    }
    
    update(star1, star2, deltaTime) {
      if (this.type === 'stream') {
        const targetStar = Math.random() > 0.5 ? star1 : star2;
        const dx = targetStar.x - this.x;
        const dy = targetStar.y - this.y;
        const dist = Math.sqrt(dx * dx + dy * dy);
        
        if (dist > 5) {
          const force = this.speed / (dist * 0.01);
          this.x += (dx / dist) * force;
          this.y += (dy / dist) * force;
        }
        
        this.angle += 0.02;
        this.x += Math.cos(this.angle) * 0.3;
        this.y += Math.sin(this.angle) * 0.3;
        
        this.life -= 0.003;
        if (this.life <= 0) {
          this.respawn(star1, star2);
        }
      } else if (this.type === 'orbit') {
        this.angle += this.speed * 0.01;
        const baseStar = Math.random() > 0.5 ? star1 : star2;
        this.x = baseStar.x + Math.cos(this.angle) * this.orbitRadius;
        this.y = baseStar.y + Math.sin(this.angle) * this.orbitRadius;
        
        this.life -= 0.002;
        if (this.life <= 0) {
          this.life = 1;
          this.orbitRadius = Math.random() * 50 + 20;
        }
      } else if (this.type === 'ambient') {
        this.twinklePhase += this.twinkleSpeed;
        this.alpha = 0.1 + Math.sin(this.twinklePhase) * 0.15;
      }
    }
    
    respawn(star1, star2) {
      const t = Math.random();
      this.x = star1.x * t + star2.x * (1 - t);
      this.y = star1.y * t + star2.y * (1 - t);
      this.life = 1;
      this.angle = Math.random() * Math.PI * 2;
    }
    
    draw(ctx) {
      const alpha = this.alpha * this.life;
      if (alpha < 0.01) return;
      
      ctx.save();
      ctx.globalAlpha = alpha;
      
      if (this.type === 'ambient') {
        ctx.fillStyle = '#ffffff';
        ctx.fillRect(this.x, this.y, this.size, this.size);
      } else {
        const gradient = ctx.createRadialGradient(
          this.x, this.y, 0,
          this.x, this.y, this.size * 3
        );
        gradient.addColorStop(0, this.type === 'stream' ? CONFIG.colorStream : '#ffffff');
        gradient.addColorStop(1, 'rgba(255,255,255,0)');
        
        ctx.fillStyle = gradient;
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size * 3, 0, Math.PI * 2);
        ctx.fill();
      }
      
      ctx.restore();
    }
  }
  
  // ============================================================================
  // STAR CLASS
  // ============================================================================
  
  class Star {
    constructor(name, color, radius, mass) {
      this.name = name;
      this.color = color;
      this.radius = radius;
      this.mass = mass;
      this.x = 0;
      this.y = 0;
      this.angle = name === 'Human' ? 0 : Math.PI;
    }
    
    update(time, barycenterX, barycenterY) {
      const orbitRadius = CONFIG.orbitScale * Math.min(width, height);
      const massRatio = this.name === 'Human' ? 0.55 : 0.45;
      const r = orbitRadius * massRatio;
      const ecc = CONFIG.eccentricity;
      const theta = this.angle;
      const effectiveRadius = r * (1 - ecc * ecc) / (1 + ecc * Math.cos(theta));
      
      this.x = barycenterX + effectiveRadius * Math.cos(theta);
      this.y = barycenterY + effectiveRadius * Math.sin(theta);
      this.angle += CONFIG.orbitSpeed * 0.01;
    }
    
    draw(ctx) {
      const glowRadius = this.name === 'Human' 
        ? CONFIG.glowRadius.human 
        : CONFIG.glowRadius.ai;
      
      // Outer glow
      ctx.save();
      ctx.globalCompositeOperation = 'screen';
      ctx.globalAlpha = CONFIG.glowIntensity * 0.3;
      const outerGlow = ctx.createRadialGradient(
        this.x, this.y, 0,
        this.x, this.y, glowRadius * 1.5
      );
      outerGlow.addColorStop(0, this.color);
      outerGlow.addColorStop(0.3, this.color);
      outerGlow.addColorStop(1, 'rgba(0,0,0,0)');
      ctx.fillStyle = outerGlow;
      ctx.beginPath();
      ctx.arc(this.x, this.y, glowRadius * 1.5, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();
      
      // Middle glow
      ctx.save();
      ctx.globalCompositeOperation = 'screen';
      ctx.globalAlpha = CONFIG.glowIntensity * 0.6;
      const midGlow = ctx.createRadialGradient(
        this.x, this.y, 0,
        this.x, this.y, glowRadius
      );
      midGlow.addColorStop(0, this.color);
      midGlow.addColorStop(0.5, this.color);
      midGlow.addColorStop(1, 'rgba(0,0,0,0)');
      ctx.fillStyle = midGlow;
      ctx.beginPath();
      ctx.arc(this.x, this.y, glowRadius, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();
      
      // Inner glow
      ctx.save();
      ctx.globalCompositeOperation = 'screen';
      ctx.globalAlpha = CONFIG.glowIntensity * 1.0;
      const innerGlow = ctx.createRadialGradient(
        this.x, this.y, 0,
        this.x, this.y, glowRadius * 0.5
      );
      innerGlow.addColorStop(0, this.color);
      innerGlow.addColorStop(1, 'rgba(0,0,0,0)');
      ctx.fillStyle = innerGlow;
      ctx.beginPath();
      ctx.arc(this.x, this.y, glowRadius * 0.5, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();
      
      // Core
      ctx.save();
      ctx.shadowColor = this.color;
      ctx.shadowBlur = 20;
      ctx.fillStyle = this.color;
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();
    }
  }
  
  // ============================================================================
  // SYSTEM STATE
  // ============================================================================
  
  let stars = [];
  let particles = [];
  
  function init() {
    resizeCanvas();
    
    stars = [
      new Star('Human', CONFIG.colorHuman, CONFIG.starRadius.human, 1.0),
      new Star('AI', CONFIG.colorAI, CONFIG.starRadius.ai, 0.9)
    ];
    
    particles = [];
    
    for (let i = 0; i < CONFIG.particles.stream; i++) {
      particles.push(new Particle(centerX, centerY, 'stream'));
    }
    
    for (let i = 0; i < CONFIG.particles.orbit; i++) {
      particles.push(new Particle(centerX, centerY, 'orbit'));
    }
    
    for (let i = 0; i < CONFIG.particles.ambient; i++) {
      particles.push(new Particle(0, 0, 'ambient'));
    }
    
    animate();
  }
  
  function resizeCanvas() {
    width = canvas.offsetWidth || window.innerWidth;
    height = canvas.offsetHeight || window.innerHeight;
    centerX = width / 2;
    centerY = height / 2;
    
    canvas.width = width * CONFIG.pixelRatio;
    canvas.height = height * CONFIG.pixelRatio;
    canvas.style.width = width + 'px';
    canvas.style.height = height + 'px';
    
    ctx.scale(CONFIG.pixelRatio, CONFIG.pixelRatio);
  }
  
  function animate() {
    time += 0.016;
    
    ctx.fillStyle = `${CONFIG.backgroundColor}${Math.round(CONFIG.trailFade * 255).toString(16).padStart(2, '0')}`;
    ctx.fillRect(0, 0, width, height);
    
    stars.forEach(star => star.update(time, centerX, centerY));
    particles.forEach(particle => {
      particle.update(stars[0], stars[1], 0.016);
      particle.draw(ctx);
    });
    stars.forEach(star => star.draw(ctx));
    
    drawGravitationalBridge();
    
    animationId = requestAnimationFrame(animate);
  }
  
  function drawGravitationalBridge() {
    const s1 = stars[0], s2 = stars[1];
    const midX = (s1.x + s2.x) / 2;
    const midY = (s1.y + s2.y) / 2;
    const dx = s2.x - s1.x;
    const dy = s2.y - s1.y;
    const dist = Math.sqrt(dx * dx + dy * dy);
    const perpX = -dy / dist;
    const perpY = dx / dist;
    
    // Breathing pulse
    const pulse = 0.7 + Math.sin(time * 0.3) * 0.3;
    
    // Layer 1: Wide soft glow (outer atmosphere)
    ctx.save();
    ctx.globalCompositeOperation = 'screen';
    ctx.globalAlpha = 0.025 * pulse;
    ctx.shadowColor = '#ffffff';
    ctx.shadowBlur = 40;
    const grad1 = ctx.createLinearGradient(s1.x, s1.y, s2.x, s2.y);
    grad1.addColorStop(0, CONFIG.colorHuman);
    grad1.addColorStop(0.5, 'rgba(255,255,255,0.6)');
    grad1.addColorStop(1, CONFIG.colorAI);
    ctx.strokeStyle = grad1;
    ctx.lineWidth = 12;
    ctx.beginPath();
    ctx.moveTo(s1.x, s1.y);
    const wave1 = Math.sin(time * 0.2) * 15;
    ctx.bezierCurveTo(
      midX + perpX * wave1 - dx * 0.15, midY + perpY * wave1 - dy * 0.15,
      midX - perpX * wave1 + dx * 0.15, midY - perpY * wave1 + dy * 0.15,
      s2.x, s2.y
    );
    ctx.stroke();
    ctx.restore();
    
    // Layer 2: Medium glow (main bridge)
    ctx.save();
    ctx.globalCompositeOperation = 'screen';
    ctx.globalAlpha = 0.04 * pulse;
    ctx.shadowColor = '#ffffff';
    ctx.shadowBlur = 20;
    const grad2 = ctx.createLinearGradient(s1.x, s1.y, s2.x, s2.y);
    grad2.addColorStop(0, CONFIG.colorHuman);
    grad2.addColorStop(0.35, 'rgba(255,255,255,0.4)');
    grad2.addColorStop(0.65, 'rgba(255,255,255,0.4)');
    grad2.addColorStop(1, CONFIG.colorAI);
    ctx.strokeStyle = grad2;
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(s1.x, s1.y);
    const wave2 = Math.sin(time * 0.25 + 0.5) * 10;
    ctx.bezierCurveTo(
      midX + perpX * wave2 - dx * 0.1, midY + perpY * wave2 - dy * 0.1,
      midX - perpX * wave2 + dx * 0.1, midY - perpY * wave2 + dy * 0.1,
      s2.x, s2.y
    );
    ctx.stroke();
    ctx.restore();
    
    // Layer 3: Thin bright core
    ctx.save();
    ctx.globalCompositeOperation = 'screen';
    ctx.globalAlpha = 0.06 * pulse;
    const grad3 = ctx.createLinearGradient(s1.x, s1.y, s2.x, s2.y);
    grad3.addColorStop(0, CONFIG.colorHuman);
    grad3.addColorStop(0.5, '#ffffff');
    grad3.addColorStop(1, CONFIG.colorAI);
    ctx.strokeStyle = grad3;
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(s1.x, s1.y);
    const wave3 = Math.sin(time * 0.3 + 1) * 6;
    ctx.bezierCurveTo(
      midX + perpX * wave3, midY + perpY * wave3,
      midX - perpX * wave3, midY - perpY * wave3,
      s2.x, s2.y
    );
    ctx.stroke();
    ctx.restore();
    
    // Layer 4: Secondary stream (offset, very subtle)
    ctx.save();
    ctx.globalCompositeOperation = 'screen';
    ctx.globalAlpha = 0.02 * pulse;
    ctx.strokeStyle = grad2;
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(s1.x, s1.y);
    const wave4 = Math.sin(time * 0.15 + 2) * 25;
    ctx.bezierCurveTo(
      midX + perpX * wave4, midY + perpY * wave4,
      midX - perpX * (wave4 * 0.5), midY - perpY * (wave4 * 0.5),
      s2.x, s2.y
    );
    ctx.stroke();
    ctx.restore();
  }
  
  // ============================================================================
  // LIFECYCLE MANAGEMENT
  // ============================================================================
  
  function destroy() {
    if (animationId) {
      cancelAnimationFrame(animationId);
    }
    window.removeEventListener('resize', handleResize);
  }
  
  function handleResize() {
    cancelAnimationFrame(animationId);
    resizeCanvas();
    animate();
  }
  
  window.addEventListener('resize', handleResize);
  
  // ============================================================================
  // START
  // ============================================================================
  
  init();
  
  // Return API for external control
  return {
    destroy,
    config: CONFIG
  };
}

// Auto-initialize if element with default ID exists
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('binary-star-bg')) {
      window.binaryStarAnimation = initBinaryStarAnimation('binary-star-bg');
    }
  });
} else {
  if (document.getElementById('binary-star-bg')) {
    window.binaryStarAnimation = initBinaryStarAnimation('binary-star-bg');
  }
}
