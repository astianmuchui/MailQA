/**
* Typewriter animation
*/

const TypeWriter = function (txtElement, words, wait = 3000) /* Create typewriter class */
{
      this.txtElement = txtElement;
      this.words = words;
      this.txt = '';
      this.wordIndex = 0;
      this.wait = parseInt(wait, 10);
      this.type();
      this.isDeleting = false;
}

TypeWriter.prototype.type = function() /* Type method */
{

      const current = this.wordIndex % this.words.length;
      const fullTxt = this.words[current];

      if (this.isDeleting)
      {
          this.txt = fullTxt.substring(0, this.txt.length - 1);
      }
      else
      {
          this.txt = fullTxt.substring(0, this.txt.length + 1);
      }

      this.txtElement.innerHTML = `<span class="txt">${this.txt}</span>`;

      typeSpeed = 80; /** Reduce this to increase speed  */

      if (this.isDeleting)
      {
          typeSpeed /= 2.5;
      }

      if (!this.isDeleting && this.txt === fullTxt)
      {
          typeSpeed = this.wait;
          this.isDeleting = true;
      }
      else if (this.isDeleting && this.txt === '')
      {
          this.isDeleting = false;
          this.wordIndex++;
          typeSpeed = 50;
      }


      setTimeout(() => this.type(), typeSpeed);
  }

  document.addEventListener('DOMContentLoaded', init);

  function init()
  {
    const txtElements = document.querySelectorAll('.txt-type');
    txtElements.forEach(txtElement => {
        const words = JSON.parse(txtElement.getAttribute('data-words'));
        const wait = txtElement.getAttribute('data-wait');
        new TypeWriter(txtElement, words, wait);
    });

}
