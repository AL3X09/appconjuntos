<script setup>
import { RouterLink} from 'vue-router'
</script>

<template>
 <!-- Navigation-->
 <div id="nav">
   <nav class="navbar navbar-expand bg-info text-uppercase text-white fixed-top" id="mainNav">
    <div class="container">
        <a class="navbar-brand" href="#">Logo</a>
            <RouterLink to="/" class="navbar-brand text-white">Nombre Proyecto</RouterLink>
            <button class="navbar-toggler text-uppercase font-weight-bold bg-primary text-white rounded" type="button" data-bs-toggle="collapse" data-bs-target="#navbarResponsive" aria-controls="navbarResponsive" aria-expanded="false" aria-label="Toggle navigation">
                     <i class="bi bi-list"></i>
            </button>
            <div class="collapse navbar-collapse" id="navbarResponsive">
                <ul class="navbar-nav ms-auto">
                    <RouterLink to="/login" class="nav-item mx-0 mx-lg-1 text-white">Ingresar</RouterLink>
                </ul>
            </div>
        </div>
    </nav>
 </div>

</template>

<style scoped>
#nav {
  padding: 27px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

</style>