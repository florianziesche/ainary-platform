(() => {
  const toggleButton = document.getElementById('feedbackToggle');
  const feedbackForm = document.getElementById('feedbackForm');
  const feedbackStatus = document.getElementById('feedbackStatus');
  const ratingStars = document.querySelectorAll('.rating-star');
  const feedbackFormElement = document.getElementById('feedbackFormElement');

  let currentRating = 0;

  const updateStatus = (message) => {
    if (feedbackStatus) {
      feedbackStatus.textContent = message;
    }
  };

  const updateRating = (rating) => {
    currentRating = rating;
    ratingStars.forEach((star) => {
      const starRating = Number(star.dataset.rating);
      star.classList.toggle('active', starRating <= rating);
      star.setAttribute('aria-pressed', starRating <= rating ? 'true' : 'false');
    });
  };

  if (toggleButton && feedbackForm) {
    toggleButton.addEventListener('click', () => {
      const isHidden = feedbackForm.hasAttribute('hidden');
      if (isHidden) {
        feedbackForm.removeAttribute('hidden');
      } else {
        feedbackForm.setAttribute('hidden', '');
      }
      toggleButton.setAttribute('aria-expanded', isHidden ? 'true' : 'false');
      toggleButton.textContent = isHidden ? 'Feedback ausblenden ▲' : 'Feedback geben ▼';
    });
  }

  ratingStars.forEach((star) => {
    star.addEventListener('click', () => {
      const rating = Number(star.dataset.rating);
      updateRating(rating);
      updateStatus(`Bewertung gesetzt: ${rating} von 5 Sternen.`);
    });
  });

  if (feedbackFormElement) {
    feedbackFormElement.addEventListener('submit', (event) => {
      event.preventDefault();
      if (currentRating === 0) {
        updateStatus('Bitte eine Bewertung auswählen.');
        return;
      }
      updateStatus('Feedback erfolgreich gesendet. Vielen Dank!');
      alert(
        '✅ Feedback erfolgreich gesendet!\n\nDer Arbeitsvorbereiter wird Ihr Feedback prüfen und bei Bedarf die Fertigungsanweisung anpassen.'
      );
      feedbackFormElement.reset();
      updateRating(0);
      if (feedbackForm && toggleButton) {
        feedbackForm.setAttribute('hidden', '');
        toggleButton.setAttribute('aria-expanded', 'false');
        toggleButton.textContent = 'Feedback geben ▼';
      }
    });
  }

  updateStatus('Bereit für Feedback.');
})();
