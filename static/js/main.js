/**
 * AMI Life Assurance — Global UI Controller
 */
document.addEventListener('DOMContentLoaded', () => {
    const navbar = document.querySelector('.premium-navbar');

    // Sticky Navbar Scroll Listener
    const handleScroll = () => {
        if (window.scrollY > 40) {
            navbar?.classList.add('navbar-scrolled');
        } else {
            navbar?.classList.remove('navbar-scrolled');
        }
    };

    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();

    // Smart Back Button Fallback
    const backBtn = document.querySelector('.back-button');
    if (backBtn) {
        backBtn.addEventListener('click', (e) => {
            // Check if user came from inside the same domain
            if (document.referrer && document.referrer.includes(window.location.host)) {
                window.history.back();
            } else {
                // Fallback route if accessed directly via link/bookmark
                window.location.href = '/'; 
            }
        });
    }
});