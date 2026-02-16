// ============================================================================
// MINIMAL SYMBOLIC BINARY STAR - EMBEDDABLE COMPONENT
// ============================================================================
// Premium minimalism: Linear/Palantir/McKinsey aesthetic
// Two elegant circles with subtle connection. Clean, geometric, restrained.
// Less is more. Premium through restraint.
// ============================================================================

function initBinaryStarMinimal(canvasId, config = {}) {
  const canvas = document.getElementById(canvasId);
  if (!canvas) {
    console.error(`Binary Star: Canvas element "${canvasId}" not found`);
    return null;
  }
  
  const ctx = canvas.getContext('2d', { alpha: true });
  
  let width, height, centerX, centerY;
  let animationId;
  let time = 0;
  
  const isMobile = window.innerWidth < 768;
  
  // ============================================================================
  // CONFIGURATION - MINIMAL & SYMBOLIC
  // ============================================================================
  
  const CONFIG = {
    // Colors
    colorHuman: config.colorHuman || '#c8aa50',
    colorAI: config.colorAI || '#e8f0ff',
    
    // Orbit
    orbitRadius: config.orbitRadius || (isMobile ? 80 : 140),
    orbitSpeed: config.orbitSpeed || 0.3,
    
    // Circles
    circleRadius: {
      human: config.circleRadiusHuman || (isMobile ? 6 : 8),
      ai: config.circleRadiusAI || (isMobile ? 5 : 7)
    },
    glowRadius: {
      human: config.glowRadiusHuman || (isMobile ? 24 : 32),
      ai: config.glowRadiusAI || (isMobile ? 20 : 28)
    },
    
    // Minimal particles
    particleCount: config.particleCount || (isMobile ? 8 : 12),
    
    // Visual
    glowIntensity: config.glowIntensity || 0.25,
    lineOpacity: config.lineOpacity || 0.12,
    
    // Background
    backgroundColor: config.backgroundColor || '#0a0a0b',
    
    // Performance
    pixelRatio: Math.min(window.devicePixelRatio, 2)
  };
  
  // ============================================================================
  // MINIMAL PARTICLE
  // ============================================================================
  
  class ConnectingParticle {
    constructor() {
      this.reset();
    }
    
    reset() {
      this.progress = Math.random();
      this.speed = 0.002 + Math.random() * 0.003;
      this.size = 1 + Math.random() * 1.5;
      this.opacity = 0.3 + Math.random() * 0.4;
    }
    
    update() {
      this.progress += this.speed;
      if (this.progress > 1) {
        this.reset();
      }
    }
    
    draw(x1, y1, x2, y2) {
      const x = x1 + (x2 - x1) * this.progress;
      const y = y1 + (y2 - y1) * this.progress;
      
      let alpha = this.opacity;
      if (this.progress < 0.1) alpha *= this.progress / 0.1;
      if (this.progress > 0.9) alpha *= (1 - this.progress) / 0.1;
      
      ctx.save();
      ctx.globalAlpha = alpha;
      
      const gradient = ctx.createRadialGradient(x, y, 0, x, y, this.size * 4);
      gradient.addColorStop(0, '#ffffff');
      gradient.addColorStop(1, 'rgba(255,255,255,0)');
      
      ctx.fillStyle = gradient;
      ctx.beginPath();
      ctx.arc(x, y, this.size * 4, 0, Math.PI * 2);
      ctx.fill();
      
      ctx.restore();
    }
  }
  
  // ============================================================================
  // STAR CIRCLE
  // ============================================================================
  
  class StarCircle {
    constructor(name, color, radius, phase) {
      this.name = name;
      this.color = color;
      this.radius = radius;
      this.phase = phase;
      this.x = 0;
      this.y = 0;
    }
    
    update(time, centerX, centerY) {
      const angle = time * CONFIG.orbitSpeed + this.phase;
      this.x = centerX + Math.cos(angle) * CONFIG.orbitRadius;
      this.y = centerY + Math.sin(angle) * CONFIG.orbitRadius;
    }
    
    draw() {
      // Single subtle glow
      ctx.save();
      ctx.globalAlpha = CONFIG.glowIntensity;
      
      const glowRadius = this.name === 'Human' 
        ? CONFIG.glowRadius.human 
        : CONFIG.glowRadius.ai;
      
      const glow = ctx.createRadialGradient(
        this.x, this.y, 0,
        this.x, this.y, glowRadius
      );
      glow.addColorStop(0, this.color);
      glow.addColorStop(0.5, this.color);
      glow.addColorStop(1, 'rgba(0,0,0,0)');
      
      ctx.fillStyle = glow;
      ctx.beginPath();
      ctx.arc(this.x, this.y, glowRadius, 0, Math.PI * 2);
      ctx.fill();
      
      ctx.restore();
      
      // Solid circle
      ctx.save();
      ctx.fillStyle = this.color;
      ctx.shadowColor = this.color;
      ctx.shadowBlur = 8;
      ctx.beginPath();
      ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();
    }
  }
  
  // ============================================================================
  // SYSTEM
  // ============================================================================
  
  let stars = [];
  let particles = [];
  
  function init() {
    resizeCanvas();
    
    stars = [
      new StarCircle('Human', CONFIG.colorHuman, CONFIG.circleRadius.human, 0),
      new StarCircle('AI', CONFIG.colorAI, CONFIG.circleRadius.ai, Math.PI)
    ];
    
    particles = [];
    for (let i = 0; i < CONFIG.particleCount; i++) {
      particles.push(new ConnectingParticle());
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
    
    // Clear (no trail - clean)
    ctx.fillStyle = CONFIG.backgroundColor;
    ctx.fillRect(0, 0, width, height);
    
    // Update stars
    stars.forEach(star => star.update(time, centerX, centerY));
    
    // Draw subtle connecting line
    ctx.save();
    ctx.globalAlpha = CONFIG.lineOpacity;
    ctx.strokeStyle = '#ffffff';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.moveTo(stars[0].x, stars[0].y);
    ctx.lineTo(stars[1].x, stars[1].y);
    ctx.stroke();
    ctx.restore();
    
    // Draw minimal particles
    particles.forEach(particle => {
      particle.update();
      particle.draw(stars[0].x, stars[0].y, stars[1].x, stars[1].y);
    });
    
    // Draw stars
    stars.forEach(star => star.draw());
    
    animationId = requestAnimationFrame(animate);
  }
  
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
  
  init();
  
  return {
    destroy,
    config: CONFIG
  };
}

// Auto-initialize
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', () => {
    if (document.getElementById('binary-star-bg')) {
      window.binaryStarAnimation = initBinaryStarMinimal('binary-star-bg');
    }
  });
} else {
  if (document.getElementById('binary-star-bg')) {
    window.binaryStarAnimation = initBinaryStarMinimal('binary-star-bg');
  }
}
