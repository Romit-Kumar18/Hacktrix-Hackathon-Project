document.addEventListener('DOMContentLoaded', function() {
    const carousel = document.querySelector('.card-carousel');
    const prevButton = document.querySelector('.prev-button');
    const nextButton = document.querySelector('.next-button');
    let scrollAmount = 0;
    const cardWidth = document.querySelector('.card').offsetWidth;
  
    nextButton.addEventListener('click', function() {
      scrollAmount += cardWidth;
      carousel.scrollTo({
        left: scrollAmount,
        behavior: 'smooth'
      });
    });
  
    prevButton.addEventListener('click', function() {
      scrollAmount -= cardWidth;
      if (scrollAmount < 0) {
        scrollAmount = 0;
      }
      carousel.scrollTo({
        left: scrollAmount,
        behavior: 'smooth'
      });
    });
  });