// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();


// client section owl carousel
$(".client_owl-carousel").owlCarousel({
    loop: true,
    margin: 20,
    dots: false,
    nav: true,
    navText: [],
    autoplay: true,
    autoplayHoverPause: true,
    navText: [
        '<i class="fa fa-angle-left" aria-hidden="true"></i>',
        '<i class="fa fa-angle-right" aria-hidden="true"></i>'
    ],
    responsive: {
        0: {
            items: 1
        },
        600: {
            items: 2
        },
        1000: {
            items: 2
        }
    }
});



/** google_map js **/
function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}








  // Initialize Locomotive Scroll
  const scroll = new LocomotiveScroll({
    el: document.querySelector('[data-scroll-container]'),
    smooth: true,
  });

  const scrollThumb = document.getElementById('scrollThumb');
  let isScrolling;

  // Update scroll thumb position during scroll
  scroll.on('scroll', (instance) => {
    const scrollPercent = instance.scroll.y / (instance.limit - window.innerHeight);
    const thumbPosition = scrollPercent * (window.innerHeight - 12);
    scrollThumb.style.top = `${thumbPosition}px`;
  });

  // Show scroll thumb on mouse move
  document.addEventListener('mousemove', () => {
    document.body.classList.add('mouse-moving');
    clearTimeout(isScrolling);
    isScrolling = setTimeout(() => {
      document.body.classList.remove('mouse-moving');
    }, 1000); // Hide the dot after 1 second of no mouse movement
  });