<template>
    <div class="privacy-policy">
      <div class="header">
        <h1>Privacy Policy</h1>
        <p class="update-info">Updated: September 22, 2024</p>
        <br />
      </div>
  
      <div class="text">
        <p>
          This Privacy Policy outlines how we handle your data, specifically concerning the collection, processing, and protection of uploaded images for the Vehicle Detection and Classification app (referred to as the Perseids). By using the Perseids, you agree to this Privacy Policy.
        </p>
        
        <h2>Data Collection</h2>
        <br />
        <p>
          When you upload images for vehicle detection and classification, we collect the following data:
        </p>
        <ul>
          <li>Image data: the actual image file you upload to the app for analysis.</li>
          <li>Metadata: information embedded within the images, such as file type and image resolution.</li>
        </ul>
        <p>
          We collect this data solely for the purpose of providing vehicle detection and classification services. We do not collect any personally identifiable information unless voluntarily provided by the user.
        </p>
        
        <h2>Data Processing</h2>
        <br />
        <p>
          The uploaded images are processed using advanced machine learning algorithms to detect and classify vehicles. The image processing is performed within our secure systems, and results are returned to you based on the images provided. 
        </p>
        <p>
          During processing:
        </p>
        <ul>
          <li>Images are stored on our servers to perform the detection and classification tasks.</li>
          <li>The data is used exclusively for vehicle detection and classification tasks and is not repurposed for any other objective.</li>
          <li>We may use aggregated and anonymized data to improve the accuracy and performance of our detection algorithms.</li>
        </ul>
        
        <h2>Data Protection</h2>
        <br />
        <p>
          We take data protection seriously and employ multiple safeguards to ensure the security of your uploaded images:
        </p>
        <ul>
          <li>Encryption: All image files are encrypted during transmission and storage to prevent unauthorized access.</li>
          <li>Access control: Only authorized personnel have access to the data, and access is granted strictly on a need-to-know basis.</li>
          <li>Retention policy: Uploaded images are retained only for the time necessary to perform detection and classification tasks. After processing is complete, images are kept in our servers unless you decide to delete them before reloading.</li>
        </ul>
        <p>
          We strive to protect your data, but please be aware that no method of transmission or electronic storage is 100% secure. While we work to safeguard your data, we cannot guarantee its absolute security.
        </p>
        <h2>Contact Information</h2>
        <br />
        <p>
          If you have any questions or concerns about the Privacy Policy or the Perseids, you can contact us at:
        </p>
        <p style="color: #02af98">
            carvarsou@alum.us.es
        </p>
  
        <p>
          By using the Perseids, you acknowledge and agree to our data collection, processing, and protection practices.
        </p>
      </div>
      <p v-for="n in 5" :key="n"><br /></p>
    </div>
</template>

<style scoped>
  .privacy-policy {
    color: #083863;
    text-align: justify;
    padding: 20px;
    width: 200%;
  }

  .header h1 {
    font-size: 2.8rem;
    margin-top: 6.5rem;
    font-weight: 500;
    text-align: center;
  }

  .update-info {
    font-size: 1rem;
    color: #6b7280;
    text-align: center;
  }

  .text h2 {
    font-size: 1.8rem;
    margin-top: 20px;
    font-weight: 500;
  }

  .text p {
    font-size: 1.3rem;
    margin-bottom: 1em;
    line-height: 1.6;
  }

  ul {
    list-style-type: disc;
    margin-left: 20px;
  }

  ul li {
    font-size: 1.3rem;
    margin-bottom: 0.5em;
  }
</style>
