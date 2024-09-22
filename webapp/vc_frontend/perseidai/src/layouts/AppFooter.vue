<template>
  <footer class="footer">
    <!-- Logo/Copyright -->
    <div class="logo">
      <span class="logo-icon">
        <img src="@/assets/icons/icon-rwh.webp" alt="Perseid.AI" />
      </span>
      <span class="logo-copyright">
        <div class="row">
          <span class="copyright-name">© 2024 - Perseid.ai </span>
        </div>
        <div class="row">
          <router-link to="/terms-of-service" class="copyright-links">Terms of Service</router-link>
          <span class="separator">⋆</span>
          <router-link to="/privacy-policy" class="privacy-links">Privacy Policy</router-link>
        </div>
      </span>
    </div>

    <!-- Navigation Links -->
    <nav class="nav-links">
      <ul>
        <li><router-link to="/models">Information about ML Models</router-link></li>
        <span class="separator">⋆</span>
        <li><router-link to="/detector/snapzone">Try Vehicle Detector</router-link></li>
        <span class="separator">⋆</span>
        <li><router-link to="/classifier/snapzone">Try Vehicle Classifier</router-link></li>
      </ul>
    </nav>

    <!-- Social Links -->
    <div class="social-links">
      <span class="github-label">PERSEID.AI</span>
      <a
        href="https://www.github.com/tfg-carvarsou/Vehicle-Classification"
        target="_blank"
        rel="noopener noreferrer"
        class="github-link"
      >
        <img src="@/assets/icons/github.svg" alt="GitHub" />
      </a>
    </div>
  </footer>
</template>

<script setup lang="ts"></script>

<style scoped>
.footer {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #080808bf;
  padding: 10px 20px;
  z-index: 1000;
  flex-wrap: wrap;
}

.logo {
  display: flex;
  align-items: center;
}

.logo img {
  height: 40px;
  margin-right: 10px;
  opacity: 0.8;
}

.logo span {
  font-size: 0.8rem;
  font-weight: bold;
  opacity: 0.8;
}

.logo .logo-copyright {
  color: #ffffff;
  opacity: 0.8;
}

.nav-links {
  display: flex;
  align-items: center;
  margin-right: 100px;
}

.nav-links ul {
  display: flex;
  justify-content: center;
  list-style: none;
  margin: 0;
  padding: 0;
  opacity: 0.8;
}

.nav-links ul li {
  margin: 0 15px;
}

.nav-links ul li a {
  font-weight: 500;
  font-size: 0.8rem;
}

.social-links {
  display: flex;
  align-items: center;
}

.github-label {
  display: flex;
  font-size: 0.8rem;
  font-weight: bold;
  opacity: 0.8;
}

.github-link {
  display: flex;
  margin-left: 4px;
  opacity: 0.5;
}

/* Responsive adjustments */
@media (max-width: 722px) {
  .footer {
    flex-direction: column;
    align-items: flex-start;
    max-height: 65vh;
  }

  .logo,
  .nav-links,
  .social-links {
    margin-bottom: 10px;
    width: 100%;
    display: flex;
    justify-content: center;
  }

  .logo {
    justify-content: flex-start;
  }

  .nav-links ul {
    display: none;
  }

  .social-links {
    justify-content: center;
  }
}
</style>
