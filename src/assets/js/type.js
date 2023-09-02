import React, { useEffect } from 'react';

// Create the TypeWriter class as a function
function TypeWriter(txtElement, words, wait = 3000) {
  this.txtElement = txtElement;
  this.words = words;
  this.txt = '';
  this.wordIndex = 0;
  this.wait = parseInt(wait, 10);
  this.type();
  this.isDeleting = false;
}

TypeWriter.prototype.type = function () {
  const current = this.wordIndex % this.words.length;
  const fullTxt = this.words[current];

  if (this.isDeleting) {
    this.txt = fullTxt.substring(0, this.txt.length - 1);
  } else {
    this.txt = fullTxt.substring(0, this.txt.length + 1);
  }

  this.txtElement.innerHTML = `<span className="txt">${this.txt}</span>`;

  let typeSpeed = 40; // Adjust this value to control typing speed

  if (this.isDeleting) {
    typeSpeed /= 2;
  }

  if (!this.isDeleting && this.txt === fullTxt) {
    typeSpeed = this.wait;
    this.isDeleting = true;
  } else if (this.isDeleting && this.txt === '') {
    this.isDeleting = false;
    this.wordIndex++;
    typeSpeed = 500;
  }

  setTimeout(() => this.type(), typeSpeed);
};

function TypeWriterComponent() {
  useEffect(() => {
    // Initialize the TypeWriter when the component mounts
    const txtElement = document.querySelector('.txt-type');
    const words = JSON.parse(txtElement.getAttribute('data-words'));
    const wait = txtElement.getAttribute('data-wait');
    new TypeWriter(txtElement, words, wait);
  }, []); // Empty dependency array to run this effect only once when the component mounts

  return (
    <div>
      <p className="txt-type" data-words='["Word1", "Word2", "Word3"]' data-wait="3000">
        {/* Initial content */}
      </p>
    </div>
  );
}

export default TypeWriterComponent;
