const markers = document.querySelectorAll('.marker');

const cb = function(entries, observer){
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('inview');
            observer.unobserve(entry.target);
        }
    });
}

const io = new IntersectionObserver(cb);

markers.forEach(marker => io.observe(marker));
