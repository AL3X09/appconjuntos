<template >
  <div v-if="getResult">
  <div v-for="result in getResult" :key="result.data.id">
  <!-- Masthead-->
        <header class="">
            <div>
              <b-card
                overlay
                img-src={{result.data.imagen}}
                img-alt="Card Image"
              >
                <b-card-text>
                  {{result.data.eslogan}}
                </b-card-text>
              </b-card>
            </div>
        </header>
        <!-- Section Noticias-->
          <b-row>
            <b-col>
              <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">Noticias</h2>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
            <div>
              <b-card
                title="Card Title"
                img-src="https://picsum.photos/600/300/?image=25"
                img-alt="Image"
                img-top
                tag="article"
                style="max-width: 20rem;"
                class="sm-12"
              >
                <b-card-text>
                  Some quick example text to build on the card title and make up the bulk of the card's content.
                </b-card-text>
                <b-button href="#" variant="primary">Go somewhere</b-button>
              </b-card>
            </div>  
            </b-col>
            <b-col>2 of 3</b-col>
            <b-col>3 of 3</b-col>
            <b-col>4 of 4</b-col>
          </b-row>
        
        <!-- Section Sección avisos ventas-->

          <b-row>
            <b-col>
              <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">Propiedades en Ventas</h2>
            </b-col>
          </b-row>
          <b-row>
            <b-col>1 of 3</b-col>
            <b-col>2 of 3</b-col>
            <b-col>3 of 3</b-col>
            <b-col>4 of 4</b-col>
          </b-row>
        <!-- Section Sección avisos arriendo-->
          <b-row>
            <b-col>
              <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">Propiedades en Arriendo</h2>
            </b-col>
          </b-row>
          <b-row>
            <b-col>1 of 3</b-col>
            <b-col>2 of 3</b-col>
            <b-col>3 of 3</b-col>
            <b-col>4 of 4</b-col>
          </b-row>

        <!-- Section Sección avisos portafolio-->
          <b-row>
            <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">Portafolio</h2>
          </b-row>
          <b-row>
            <b-col>1 of 3</b-col>
            <b-col>2 of 3</b-col>
            <b-col>3 of 3</b-col>
            <b-col>4 of 4</b-col>
          </b-row>
        <!-- About Section-->
        <section class="page-section bg-primary text-white mb-0" id="about">
                <!-- About Section Heading-->
                <h2 class="page-section-heading text-center text-uppercase text-white">Acerca de nosotros</h2>
                <!-- Icon Divider-->
                <div class="divider-custom divider-light">
                    <div class="divider-custom-line"></div>
                    <div class="divider-custom-icon"><i class="fas fa-star"></i></div>
                    <div class="divider-custom-line"></div>
                </div>
                <!-- About Section Content-->
                <div class="row">
                    <div class="col-sm12"><p class="lead">{{result.data.about}}</p></div>
                </div>
                
        </section>
        <!-- Section salon comunal-->
          <b-row>
            <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">Salon Comunal</h2>
          </b-row>
          <b-row>
            <b-col>1 of 3</b-col>
            <b-col>2 of 3</b-col>
          </b-row>
          <!-- Contact Section-->
          <!-- Contact Section Heading-->
          <b-row>
            <b-col>
             <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">Contactenos</h2>
            </b-col>
          </b-row>
          <b-row>
            <b-col sm="12" lg="6">
              <p class="lead">{{result.data.adress}}</p>
              <p class="lead">{{result.data.email}}</p>
              <p class="lead">{{result.data.telephone}}</p>
            </b-col>
              <b-col sm="12" lg="6">
                <form id="contactForm" data-sb-form-api-token="API_TOKEN">
                        <!-- Name input-->
                        <div class="form-floating mb-3">
                            <input class="form-control" id="name" type="text" placeholder="Enter your name..." data-sb-validations="required" />
                            <label for="name">Full name</label>
                            <div class="invalid-feedback" data-sb-feedback="name:required">A name is required.</div>
                        </div>
                        <!-- Email address input-->
                        <div class="form-floating mb-3">
                            <input class="form-control" id="email" type="email" placeholder="name@example.com" data-sb-validations="required,email" />
                            <label for="email">Email address</label>
                            <div class="invalid-feedback" data-sb-feedback="email:required">An email is required.</div>
                            <div class="invalid-feedback" data-sb-feedback="email:email">Email is not valid.</div>
                        </div>
                        <!-- Phone number input-->
                        <div class="form-floating mb-3">
                            <input class="form-control" id="phone" type="tel" placeholder="(123) 456-7890" data-sb-validations="required" />
                            <label for="phone">Phone number</label>
                            <div class="invalid-feedback" data-sb-feedback="phone:required">A phone number is required.</div>
                        </div>
                        <!-- Message input-->
                        <div class="form-floating mb-3">
                            <textarea class="form-control" id="message" type="text" placeholder="Enter your message here..." style="height: 10rem" data-sb-validations="required"></textarea>
                            <label for="message">Message</label>
                            <div class="invalid-feedback" data-sb-feedback="message:required">A message is required.</div>
                        </div>
                        <!-- Submit success message-->
                        <!---->
                        <!-- This is what your users will see when the form-->
                        <!-- has successfully submitted-->
                        <div class="d-none" id="submitSuccessMessage">
                            <div class="text-center mb-3">
                                <div class="fw-bolder">Form submission successful!</div>
                                To activate this form, sign up at
                                <br />
                                <a href="https://startbootstrap.com/solution/contact-forms">https://startbootstrap.com/solution/contact-forms</a>
                            </div>
                        </div>
                        <!-- Submit error message-->
                        <!---->
                        <!-- This is what your users will see when there is-->
                        <!-- an error submitting the form-->
                        <div class="d-none" id="submitErrorMessage"><div class="text-center text-danger mb-3">Error sending message!</div></div>
                        <!-- Submit Button-->
                        <button class="btn btn-primary btn-xl disabled" id="submitButton" type="submit">Send</button>
                    </form>
              </b-col>
          </b-row>
          <!-- Icon Divider-->
          <div class="divider-custom">
              <div class="divider-custom-line"></div>
              <div class="divider-custom-icon"><i class="fas fa-star"></i></div>
              <div class="divider-custom-line"></div>
          </div>
          <!-- Contact Section Form-->
          <div class="row justify-content-center">
              <div class="col-lg-8 col-xl-7"> </div>
          </div>
        <br/>
    </div>
  </div>
  <div v-else>
    <b-card-text>
     Error conectando al servidor no se presentan datos
    </b-card-text>
  </div>
</template>

<script>
//https://www.positronx.io/handle-ajax-requests-in-vue-js-with-axios-fetch-api/
//https://www.koderhq.com/tutorial/vue/http-axios/
//https://www.bezkoder.com/vue-axios-example/
import http from "../http-common";
//import { ref, onMounted  } from 'vue'

export default {
  data() {
    return {
      respon: [],
      dataconjunto: [],
      getResult: [],
    }
  },
  mounted() {
    this.getAllData();
    //console.log(this.getResult);
  },
  methods: {
    fortmatResponse(res) {
      return JSON.stringify(res, null, 2);
    },
    async getAllData() {
      try {
        const res = await http.get("conjunto/api/detalle/1/");
        const result = {
          status: res.status + "-" + res.statusText,
          //headers: res.headers,
          data: res.data,
        };
        this.getResult.push(result);
      } catch (err) {
        this.getResult.push(this.fortmatResponse(err.response?.data) || err);
        //this.getResult = this.fortmatResponse(err.response?.data) || err;
      }
    },
    clearGetOutput() {
      this.getResult = null;
    },
  }
};

</script>
<style>
.row {
  --bs-gutter-x: -1.5rem !important;
}
</style>
