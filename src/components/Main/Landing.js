import React from 'react';
import envelopeImage from '../../assets/img/envelope.png';
import mailcartImage from '../../assets/img/mailcart.png';
import scanImage from '../../assets/img/scan.png';

function Landing() {
  return (
    <>
      <main className="showcase">
        <div className="grid-2">
          <img src={envelopeImage} alt="" height="95%" />
          <div className="text">
            <h1 className="txt-gradient txt-light">Scanning through emails was the old thing.</h1>
            <p className="txt-grey">
              In a world where our inboxes are constantly inundated with messages from work, family, friends, and subscriptions, maintaining email sanity can be a daunting task.
              This is where we come in
            </p>
            <a href="./signup" className="btn-gradient">Sign up now</a>
          </div>
        </div>
      </main>

      <section className="showcase">
        <div className="grid-2">
          <div className="text">
            <h1 className="txt-gradient txt-light">We are here to declutter your inbox</h1>
            <p className="txt-grey">
              Our algorithm is dedicated to simplifying your digital life, providing you with the means to declutter, prioritize, and organize your emails effortlessly. Whether you're a busy professional, a student, or anyone seeking email tranquility, we're at your service.
            </p>
            <a href="./signup" className="btn-gradient">Register now</a>
          </div>
          <img src={mailcartImage} alt="" height="90%" />
        </div>
      </section>

      <section className="showcase">
        <div className="grid-2">
          <img src={scanImage} alt="" height="90%" />
          <div className="text">
            <h1 className="txt-gradient txt-light">Find What You Need and boost your productivity </h1>
            <p className="txt-grey">
              Say goodbye to wasted hours and hello to a productivity boost that transforms the way you work. Reclaim your time and make the most out of every email.
            </p>
            <a href="./signup" className="btn-gradient">Get started</a>
          </div>
        </div>
      </section>
    </>
  )
}

export default Landing;
