<template>
  <header class="header">
    <!-- Logo/Title -->
    <div class="logo">
      <router-link to="/" class="logo-icon">
        <img src="@/assets/icons/icon.webp" alt="Perseid.AI" />
      </router-link>
      <router-link to="/" class="logo-title">
        <span class="title-perseid">Perseid.</span>
        <span class="title-ai"><i>AI</i></span>
      </router-link>
    </div>

    <!-- Navigation Menu -->
    <div :class="{'menu-open': isMenuOpen }" class="nav-menu">
      <nav class="nav-links">
        <ul>
          <li><router-link to="/models">Models</router-link></li>
          <li><router-link to="/detector">Detector</router-link></li>
          <li><router-link to="/classificator">Classificator</router-link></li>
          <li><router-link to="/faq">FAQ</router-link></li>
        </ul>
      </nav>
      <!-- Auth Links for mobile -->
      <nav class="auth-links-mobile">
        <ul>
          <li><router-link to="/login" class="login-btn">Log in</router-link></li>
          <li><router-link to="/signup" class="signup-btn">Sign up</router-link></li>
        </ul>
      </nav>
    </div>

    <!-- Auth Links for desktop -->
    <div class="auth-links-desktop">
      <router-link to="/login" class="login-btn">Log in</router-link>
      <router-link to="/signup" class="signup-btn">Sign up</router-link>
    </div>

    <!-- Toggle Menu Button -->
    <div class="toggle-menu" @click="toggleMenu">
      ☰
    </div>
  </header>
</template>

<script>
  export default {
    name: 'AppHeader',
    data() {
      return {
        isMenuOpen: false,
      };
    },
    methods: {
      toggleMenu() {
        this.isMenuOpen = !this.isMenuOpen;
      },
    },
  };
</script>

<style scoped>
.header {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #DEEDF5;
  padding: 10px 20px;
  z-index: 1000;
}

.logo {
  display: flex;
  align-items: center;
}

.logo img {
  height: 40px;
  margin-right: 10px;
}

.logo span {
  font-size: 1.5rem;
  font-weight: bold;
}

.logo .title-perseid {
  color: #083863;
}

.logo .title-ai {
  color: #02AF98;
}

.nav-menu {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-grow: 1;
}

.nav-links ul {
  display: flex;
  list-style: none;
  margin: 0;
  padding: 0;
}

.nav-links ul li {
  margin: 0 15px;
}

.nav-links ul li a {
  text-decoration: none;
  color: #083863;
  font-weight: 500;
}

.auth-links-mobile ul {
  display: none;
}

.auth-links-desktop {
  display: flex;
  align-items: center;
}

.auth-links-desktop a {
  margin-left: 15px;
  text-decoration: none;
}

.login-btn {
  color: #083863;
}

.signup-btn {
  background-color: #02AF98;
  color: white;
  padding: 5px 10px;
  border-radius: 5px;
}

.toggle-menu {
  display: none;
  font-size: 24px;
  cursor: pointer;
}

@media (max-width: 722px) {
  .nav-menu {
    display: none;
    position: absolute;
    top: 60px;
    left: 0;
    width: 100%;
    background-color: #F1F5F9;
    flex-direction: column;
    align-items: flex-start;
  }

  .menu-open {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
  }

  .nav-links ul, .auth-links-mobile ul {
    flex-direction: column;
    width: 100%;
    display: block;
  }

  .nav-links ul li, .auth-links-mobile ul li {
    margin: 10px 0;
    width: 100%;
  }

  .nav-links ul li a, .auth-links-mobile ul li a {
    padding: 10px 20px;
    width: 100%;
    display: block;
  }

  .auth-links-desktop {
    display: none;
  }

  .toggle-menu {
    display: block;
    color: #083863;
  }
}
</style>
