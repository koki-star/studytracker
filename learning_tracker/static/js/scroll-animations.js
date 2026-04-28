/* ============================================
   SCROLL ANIMATIONS & INTERACTIONS
   Enhanced scroll effects with Intersection Observer
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {
    initScrollAnimations();
    initParallax();
    initCardEffects();
    initSmoothScroll();
});

/* ============================================
   INTERSECTION OBSERVER FOR ANIMATIONS
   Fallback for browsers without scroll-timeline support
   ============================================ */

function initScrollAnimations() {
    // Check if browser supports scroll-timeline
    const supportsScrollTimeline = CSS.supports('animation-timeline', 'scroll()');
    
    if (supportsScrollTimeline) {
        // Native scroll-timeline support - CSS handles it
        return;
    }
    
    // Fallback: Use Intersection Observer
    const animatedElements = document.querySelectorAll(
        '.fade-up, .scale-in, .slide-in-left, .slide-in-right, .blur-in'
    );
    
    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animated');
                }
            });
        },
        {
            threshold: 0.1,
            rootMargin: '0px 0px -100px 0px'
        }
    );
    
    animatedElements.forEach(el => observer.observe(el));
}

/* ============================================
   PARALLAX SCROLLING
   Smooth parallax effect for background elements
   ============================================ */

function initParallax() {
    const parallaxElements = document.querySelectorAll('.parallax-slow, .parallax-fast');
    
    if (parallaxElements.length === 0) return;
    
    // Throttle for performance
    let ticking = false;
    
    window.addEventListener('scroll', () => {
        if (!ticking) {
            window.requestAnimationFrame(() => {
                const scrolled = window.pageYOffset;
                
                parallaxElements.forEach(el => {
                    const speed = el.classList.contains('parallax-slow') ? 0.5 : 1.5;
                    const yPos = -(scrolled * speed);
                    el.style.transform = `translateY(${yPos}px)`;
                });
                
                ticking = false;
            });
            ticking = true;
        }
    });
}

/* ============================================
   CARD HOVER EFFECTS
   3D tilt effect on mouse move
   ============================================ */

function initCardEffects() {
    const cards = document.querySelectorAll('.card');
    
    cards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            const rotateX = (y - centerY) / 20;
            const rotateY = (centerX - x) / 20;
            
            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-8px)`;
        });
        
        card.addEventListener('mouseleave', () => {
            card.style.transform = '';
        });
    });
}

/* ============================================
   SMOOTH SCROLLING
   Enhanced smooth scroll with easing
   ============================================ */

function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            
            if (targetId === '#') return;
            
            const target = document.querySelector(targetId);
            
            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

/* ============================================
   ANIMATED COUNTERS
   Number animation on scroll into view
   ============================================ */

function animateCounter(element, target, duration = 2000) {
    let start = 0;
    const increment = target / (duration / 16);
    
    const timer = setInterval(() => {
        start += increment;
        if (start >= target) {
            element.textContent = Math.floor(target);
            clearInterval(timer);
        } else {
            element.textContent = Math.floor(start);
        }
    }, 16);
}

// Initialize counters when in viewport
const counterObserver = new IntersectionObserver(
    (entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const target = parseInt(entry.target.dataset.target);
                animateCounter(entry.target, target);
                counterObserver.unobserve(entry.target);
            }
        });
    },
    { threshold: 0.5 }
);

document.querySelectorAll('.stat-number[data-target]').forEach(el => {
    counterObserver.observe(el);
});

/* ============================================
   LOADING ANIMATIONS
   Fade in page content on load
   ============================================ */

window.addEventListener('load', () => {
    document.body.classList.add('loaded');
});
