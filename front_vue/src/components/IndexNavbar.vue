
<template>

  <div v-if="vgetHead">
    <div v-for="resulth in vgetHead" :key="resulth.data.id">
        <!-- Navigation-->
        <div id="nav">
          <nav class="navbar navbar-expand bg-info text-uppercase text-white fixed-top" id="mainNav">
            <div class="container">
                <a class="navbar-brand" href="#"><b-img src= "/public/img/ + '{{resulth.data.logo.slice(70)}}'" fluid alt="Fluid image"></b-img></a>
                    <RouterLink to="/" class="navbar-brand text-white"> {{resulth.data.name}} b</RouterLink>
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
    </div>
  </div>
  <div v-else>
    <b-card-text>
     Error conectando al servidor no se presentan datos
    </b-card-text>
  </div>

</template>

<script>
import { RouterLink} from 'vue-router'
//https://www.positronx.io/handle-ajax-requests-in-vue-js-with-axios-fetch-api/
//https://www.koderhq.com/tutorial/vue/http-axios/
//https://www.bezkoder.com/vue-axios-example/
import http from "../http-common";

export default {
  
  data() {
    return {
      vgetHead: [],
    }
  },
  mounted() {
    this.getHead();
  },
  methods: {
    fortmatResponse(res) {
      return JSON.stringify(res, null, 2);
    },
    async getHead() {
      try {
        const res = await http.get("conjunto/api/nombre/1/");
        const result = {
          status: res.status + "-" + res.statusText,
          //headers: res.headers,
          data: res.data[0],
        };
        this.vgetHead.push(result);
      } catch (err) {
        this.vgetHead.push(this.fortmatResponse(err.response?.data) || err);
        //this.getResult = this.fortmatResponse(err.response?.data) || err;
      }
    },
    clearGetOutput() {
      this.vgetHead = null;
    },
  }
};

</script>


<style scoped>
#nav {
  padding: 27px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

</style>