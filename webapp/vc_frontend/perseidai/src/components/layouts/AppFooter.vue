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
    </footer>
</template>

<script setup lang="ts">
</script>

<style scoped>
.footer {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #08080800;
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
  font-size: 0.8rem;
  font-weight: bold;
  opacity: 0.80;
}

.logo .logo-copyright {
  color: #ffffff;
}
</style>