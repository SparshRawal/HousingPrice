<template>
  <div class="box">
  
  <div >
        <div class="row">
            <h1 class="text-center text-secondary">We need some details about your property</h1>
        </div>
        <form @submit.prevent="submitForm" id="myform">
          <div class="search-box">
      
    </div>    
            <div class="container-fluid row mx-auto col-12 col-md-10 col-lg-10" id="App">
              <div class="mb-3 mt-4 pt-4 row">
                
                <div class="col-sm-12">
                <GMapMap :center="coords" :zoom="13" map-type-id="terrain" style="width: 100%; height: 20rem" class="bg-dark text-secondary border-secondary" >
                  <!-- Marker to display the searched location -->
                  <GMapMarker
                    :key="markerDetails.id"
                    :position="markerDetails.position"
                    :clickable="true"
                    :draggable="false"
                    @click="openMarker(markerDetails.id)"
                  >
                    <!-- InfoWindow to display the searched location details -->
                      <GMapInfoWindow
                        v-if="locationDetails.address != ''"
                        :closeclick="true"
                        @closeclick="openMarker(null)"
                        :opened="openedMarkerID === markerDetails.id"
                        :options="{
                          pixelOffset: {
                            width: 10,
                            height: 0
                          },
                          maxWidth: 320,
                          maxHeight: 320
                        }"
                      
                      >
                        <div class="location-details bg-dark btn-outline-secondary">
                          <h3>Location Details</h3>
                          <p>Address: {{ locationDetails.address }}</p>
                          <p>
                            URL: <a :href="locationDetails.url" target="_blank"> {{ locationDetails.url }}</a>
                          </p>
                        </div>
                      </GMapInfoWindow>
                      
                  </GMapMarker>
                  </GMapMap>
                </div>
                <div class="col sm-1"></div>

              </div>
              <div class="row mb-3 mt-4 pt-4">
                <div class="col-sm-2"></div>
                
                  <GMapAutocomplete
                placeholder="Search your Property"
                @place_changed="setPlace"
                style="font-size: large"
                class="col-sm-9 btn-outline-primary bg-dark text-secondary border-secondary"
              >
              </GMapAutocomplete>
                
                <div class="col-sm-2"></div>
              
              </div>
                <div class="mb-3 mt-4 pt-4 row">
                    <label for="staticEmail" class="col-sm-1 pt-2 col-form-label border-dark text-secondary">Latitude</label>
                    <div class="col-sm-2">
                      <label class="btn btn-outline-primary mt-2 disabled" >{{coords.lat}}</label>

                    </div>
                    <label for="staticEmail" class="col-sm-1 pt-2 col-form-label border-dark text-secondary">Longitude</label>
                    <div class="col-sm-2">
                      <label class="btn btn-outline-primary mt-2 disabled" >{{coords.lng}}</label>

                    </div>
                    <label for="staticEmail" class="col-sm-1 pt-2 col-form-label border-dark text-secondary">Zipcode</label>
                    <div class="col-sm-2">
                      <input type="number" class="form-control-sm  mt-2 border-primary bg-dark text-secondary" id="username"
                          placeholder="Enter ZIP" v-model="ZIP" required min="1" max="99999" step="1"/>

                    </div>
                    <label for="staticEmail" class="col-sm-1 pt-2 col-form-label border-dark text-secondary">Square Footage</label>
                    <div class="col-sm-2">
                      <input type="number" class="form-control-sm  mt-2 border-primary bg-dark text-secondary" id="username"
                          placeholder="Enter ZIP" v-model="SQFT" required min="1" max="9999" step="1"/>
                    </div>
                    
                </div>
                <div class="mb-3 mt-2 pt-2 row">
                  <div class="col-sm-2">

                  <label for="staticEmail" class="col-form-label border-dark text-secondary">How are you Using the House?</label>
                  </div>
                  <div class="col-sm-2 mt-2">
                      <select class="form-select bg-dark border-secondary text-secondary" aria-label="Default select example" v-model = "IntendedUse">
                        <option  selected value="PrimaryRes">Primary residence</option>
                        <option value="Rental">Renting to someone</option>
                        <option value="NonPrimary">Non Primary residence</option>
                        <option value="Unknown">Other</option>
                    </select>
                  </div>
                  <div class="col-sm-2">

                    <label for="staticEmail" class="col-form-label border-dark text-secondary">What's the type of your Deed?</label>
                    </div>
                    <div class="col-sm-2 mt-2">
                        <select class="form-select bg-dark border-secondary text-secondary" aria-label="Default select example" v-model = "Deed">
                          <option  selected value="Warranty Deed">Warranty Deed</option>
                          <option value="Joint Tenancy Deed">Joint Tenancy Deed</option>
                          <option value="Quit Claim Deed">Quit Claim Deed</option>
                          <option value="Contract or Agreement">Contract or Agreement</option>
                          <option value="Other">Other</option>
                      </select>
                    </div>
                    <div class="col-sm-2 col-form-label text-secondary">
                        Your Financing?
                    </div>
                    <div class="btn-group pb-4 col-sm-2" role="group" aria-label="Basic radio toggle button group 1">
                        <input type="radio" class="btn-check btn-sm" name="btnradioA" id="btnradio1" autocomplete="off" checked value="Cash" v-model="this.Financing">
                        <label class="btn btn-outline-primary col-sm-2 mt-2 mb-2 btn-sm" for="btnradio1">Cash</label>

                        <input type="radio" class="btn-check btn-sm" name="btnradioA" id="btnradio2" autocomplete="off" value="Other" v-model="this.Financing">
                        <label class="btn btn-outline-secondary col-sm-2 mt-2 mb-2 btn-sm" for="btnradio2">Other</label>
                    </div>
                </div>
                <div class="mb-3 mt-2 pt-2 row">       
                    <div class="col-sm-2 col-form-label text-secondary">
                        Do you know the buyer?
                    </div>
                    <div class="btn-group pb-4 col-sm-2" role="group" aria-label="Basic radio toggle button group 2">
                        <input type="radio" class="btn-check btn-sm" name="btnradioB" id="btnradio3" autocomplete="off"  value="Yes" v-model="this.BuyerSellerRelated">
                        <label class="btn btn-outline-primary col-sm-2 mt-2 mb-2 btn-sm" for="btnradio3">Yes</label>

                        <input type="radio" class="btn-check btn-sm" name="btnradioB" id="btnradio4" autocomplete="off" checked value="No" v-model="this.BuyerSellerRelated">
                        <label class="btn btn-outline-secondary col-sm-2 mt-2 mb-2 btn-sm" for="btnradio4">No</label>
                    </div>
                    <div class="col-sm-2 col-form-label text-secondary">
                        Do you have solar power?
                    </div>
                    <div class="btn-group pb-4 col-sm-2" role="group" aria-label="Basic radio toggle button group">
                        <input type="radio" class="btn-check btn-sm" name="btnradioC" id="btnradio5" autocomplete="off"  value="Yes" v-model="this.Solar">
                        <label class="btn btn-outline-primary col-sm-2 mt-2 mb-2 btn-sm" for="btnradio5">Yes</label>

                        <input type="radio" class="btn-check btn-sm" name="btnradioC" id="btnradio6" autocomplete="off" checked value="No" v-model="this.Solar">
                        <label class="btn btn-outline-secondary col-sm-2 mt-2 mb-2 btn-sm" for="btnradio6">No</label>
                    </div>
                    <div class="col-sm-1 col-form-label text-secondary">
                        Personal property?
                    </div>
                    <div class="btn-group pb-4 col-sm-2" role="group" aria-label="Basic radio toggle button group">
                        <input type="radio" class="btn-check btn-sm" name="btnradioD" id="btnradio7" autocomplete="off" checked value="Yes" v-model="this.PersonalProperty">
                        <label class="btn btn-outline-primary col-sm-2 mt-2 mb-2 btn-sm" for="btnradio7">Yes</label>

                        <input type="radio" class="btn-check btn-sm" name="btnradioD" id="btnradio8" autocomplete="off" value="No" v-model="this.PersonalProperty">
                        <label class="btn btn-outline-secondary col-sm-2 mt-2 mb-2 btn-sm" for="btnradio8">No</label>
                    </div>
                </div>
                <div class="mb-3 mt-2 pt-2 row">       
                    <div class="col-sm-2 col-form-label text-secondary">
                        Partial Interest?
                    </div>
                    <div class="btn-group pb-4 col-sm-2" role="group" aria-label="Basic radio toggle button group 2">
                        <input type="radio" class="btn-check btn-sm" name="btnradioE" id="btnradio9" autocomplete="off"  value="Yes" v-model="this.PartialInterest">
                        <label class="btn btn-outline-primary col-sm-2 mt-2 mb-2 btn-sm" for="btnradio9">Yes</label>

                        <input type="radio" class="btn-check btn-sm" name="btnradioE" id="btnradio10" autocomplete="off" checked value="No" v-model="this.PartialInterest">
                        <label class="btn btn-outline-secondary col-sm-2 mt-2 mb-2 btn-sm" for="btnradio10">No</label>
                    </div>
                    <div class="col-sm-3">

                      <label for="staticEmail" class="col-form-label border-dark text-secondary">Overall How would you rate the condition of the house?</label>
                      </div>
                      <div class="col-sm-2 mt-2">
                          <select class="form-select bg-dark border-secondary text-secondary" aria-label="Default select example" v-model = "CLASS">
                            <option value="1">Needs refurbishing</option>
                            <option value="2">Some issues</option>
                            <option selected value="3">Livable</option>
                            <option value="4">Good</option>
                            <option value="5">Great</option>
                            <option value="6">Excellent</option>
                        </select>
                      </div>
                      <div class="col-sm-2">

                        <label for="staticEmail" class="col-form-label border-dark text-secondary">How many Garages do you Have?</label>
                        </div>
                        <div class="col-sm-1 mt-2 pb-4">

                        <input type="number" class="form-control-sm border-primary bg-dark text-secondary" id="username"
                            placeholder="Max 9" v-model="GARAGE" required min="1" max="9" step="1"/>
                        </div>
                    
                </div>
                <div class="mb-3 mt-2 pt-2 row">       
                  <div class="col-sm-2">

                  <label for="staticEmail" class="col-form-label border-dark text-secondary">How many floors?</label>
                  </div>
                  <div class="col-sm-1 mt-2">
                      <select class="form-select bg-dark border-primary text-secondary" aria-label="Default select example" v-model = "STORIES">
                        <option value="1">1</option>
                        <option value="1.5">1.5</option>
                        <option selected value="2">2</option>
                        <option value="2.5">2.5</option>
                        <option value="3">3</option>
                    </select>
                  </div>
                    <div class="col-sm-2">

                      <label for="staticEmail" class="col-form-label border-dark text-secondary">How many Rooms?</label>
                      </div>
                      <div class="col-sm-1 mt-2 pb-4">
                      
                      <input type="number" class="form-control-sm border-primary bg-dark text-secondary" id="username"
                          placeholder="Max 12" v-model="ROOMS" required min="1" max="12" step="1"/>
                  </div>
                  <div class="col-sm-3">
                    <label for="staticEmail" class="col-form-label border-dark text-secondary">What's the condition of the rooms?</label>
                    </div>
                    <div class="col-sm-2 mt-2">
                        <select class="form-select bg-dark border-primary text-secondary" aria-label="Default select example" v-model = "QUALITY">
                          <option value="1">Needs Repaint</option>
                          <option value="2">Good</option>
                          <option selected value="3">Very Good</option>
                          <option value="4">Excellent</option>
                      </select>
                    </div>
                    
                </div>
                <div class="mb-3 mt-2 pt-2 row">       
                    <div class="col-sm-2">

                      <label for="staticEmail" class="col-form-label border-dark text-secondary">How many Heaters do you have?</label>
                      </div>
                      <div class="col-sm-1 mt-2 pb-4">
                      
                      <input type="number" class="form-control-sm border-primary bg-dark text-secondary" id="username"
                          placeholder="Max 9" v-model="HEAT" required min="1" max="9" step="1"/>
                  </div>
                  <div class="col-sm-2">
                  <label for="staticEmail" class="col-form-label border-dark text-secondary">How many Cooling Units do you have?</label>
                  </div>
                  <div class="col-sm-1 mt-2 pb-4">

                  <input type="number" class="form-control-sm border-primary bg-dark text-secondary" id="username"
                      placeholder="Max 9" v-model="COOL" required min="0" max="9" step="1"/>
                  </div>
                  <div class="col-sm-3">
                  <label for="staticEmail" class="col-form-label border-dark text-secondary">Number of Bathroom Fixtures?</label>
                  </div>
                  <div class="col-sm-1 mt-2 pb-4">

                  <input type="number" class="form-control-sm border-primary bg-dark text-secondary" id="username"
                      placeholder="Max 30" v-model="BATHFIXTUR" required min="1" max="30" step="1"/>
                  </div>             
                </div>
                <div class="mb-3 mt-2 pt-2 row">       
                    <div class="col-sm-2 col-form-label text-secondary">
                        Are you a 
                    </div>
                    <div class="btn-group pb-4 col-sm-4" role="group" aria-label="Basic radio toggle button group 2">
                        <input type="radio" class="btn-check btn-sm" name="btnradioF" id="btnradio11" autocomplete="off" checked  value="Buyer" v-model="this.buyerSeller">
                        <label class="btn btn-outline-primary col-sm-3 mt-2 mb-2 btn-lg" for="btnradio11">Buyer</label>

                        <input type="radio" class="btn-check btn-sm" name="btnradioF" id="btnradio12" autocomplete="off"  value="Seller" v-model="this.buyerSeller">
                        <label class="btn btn-outline-secondary col-sm-3 mt-2 mb-2 btn-lg" for="btnradio12">Seller</label>
                    </div>
                    <div class="col-sm-2" v-if="this.buyerSeller == 'Seller'">
                  <label for="staticEmail" class="col-form-label border-dark text-secondary">Enter price at which you bought the property</label>
                  </div>
                  <div class="col-sm-4 btn" v-if="this.buyerSeller == 'Seller'">

                  <input type="number" class="form-control border-primary bg-dark text-secondary btn" id="username"
                      placeholder="Enter Price" v-model="this.cost" required min="1" max="" step="1"/>
                  </div>
                    
                </div>
                <div class="mb-3 row">
                  <button class="btn btn-outline-success" type="submit" form="myform">
                      Check Price Now!
                  </button>
                </div>
            </div>
        </form>
    </div>

    </div>
</template>

<script>

import '@vuepic/vue-datepicker/dist/main.css';
import axios from "axios";
import { onMounted, ref } from 'vue'
// import { GoogleMap, Marker } from "vue3-google-map";

export default {
    name: "RegisterPage",
    setup() {
    // Setting the default coordinates to London
    const coords = ref({ lat: 51.5072, lng: 0.1276 })
    // Marker Details
    const markerDetails = ref({
      id: 1,
      position: coords.value
    })
    const openedMarkerID = ref(null)

    // Places Details
    const locationDetails = ref({
      address: '',
      url: ''
    })

    // Get users current location using the browser's geolocation API
    const getUserLocation = () => {
      // Check if Geolocation is supported by the browser
      const isSupported = 'navigator' in window && 'geolocation' in navigator
      if (isSupported) {
        // Retrieve the user's current position
        navigator.geolocation.getCurrentPosition((position) => {
          coords.value.lat = position.coords.latitude
          coords.value.lng = position.coords.longitude
        })
      }
    }
    // Set the location based on the place selected
    const setPlace = (place) => {
      coords.value.lat = place.geometry.location.lat()
      coords.value.lng = place.geometry.location.lng()

      // Update the location details
      locationDetails.value.address = place.formatted_address
      locationDetails.value.url = place.url
    }

    // Open the marker info window
    const openMarker = (id) => {
      openedMarkerID.value = id
    }

    onMounted(() => {
      getUserLocation()
    })

    return {
      coords,
      markerDetails,
      openedMarkerID,
      openMarker,
      getUserLocation,
      setPlace,
      locationDetails
    }
  },
    data() {
        return {
          IntendedUse: "PrimaryRes",
          Deed: "Warranty Deed",
          Financing: "Other",
          BuyerSellerRelated: "No",
          Solar: "No",
          PersonalProperty: "Yes",
          PartialInterest: "No",
          CLASS : 3,
          STORIES: 1,
          ROOMS: 5,
          QUALITY: 2,
          HEAT: 4,
          COOL: 2,
          BATHFIXTUR: 15,
          SQFT: 1,
          GARAGE: 1,
          LON: 0,
          LAT: 0,
          ZIP: 78746,
          buyerSeller: "Buyer",
          cost: 0,
        };
    },
    methods: {        
        submitForm() {
            const formData = {
                      IntendedUse: this.IntendedUse,
                      Deed: this.Deed,
                      Financing: this.Financing,
                      BuyerSellerRelated: this.BuyerSellerRelated,
                      Solar: this.Solar,
                      PersonalProperty: this.PersonalProperty,
                      PartialInterest: this.PartialInterest,
                      CLASS: this.CLASS,
                      STORIES: this.STORIES,
                      ROOMS: this.ROOMS,
                      QUALITY: this.QUALITY,
                      HEAT: this.HEAT,
                      COOL: this.COOL,
                      BATHFIXTUR: this.BATHFIXTUR,
                      SQFT: this.SQFT,
                      GARAGE: this.GARAGE,
                      LON: this.coords.lng,
                      LAT: this.coords.lat,
                      ZIP: this.ZIP,
            };
            
            let form_Data = new FormData()
            form_Data.append('IntendedUse', formData.IntendedUse);
            form_Data.append('Deed', formData.Deed);
            form_Data.append('Financing', formData.Financing);
            form_Data.append('BuyerSellerRelated', formData.BuyerSellerRelated);
            form_Data.append('Solar', formData.Solar);
            form_Data.append('PersonalProperty', formData.PersonalProperty);
            form_Data.append('PartialInterest', formData.PartialInterest);
            form_Data.append('CLASS', formData.CLASS);
            form_Data.append('STORIES', formData.STORIES);
            form_Data.append('ROOMS', formData.ROOMS);
            form_Data.append('QUALITY', formData.QUALITY);
            form_Data.append('HEAT', formData.HEAT);
            form_Data.append('COOL', formData.COOL);
            form_Data.append('BATHFIXTUR', formData.BATHFIXTUR);
            form_Data.append('SQFT', formData.SQFT);
            form_Data.append('GARAGE', formData.GARAGE);
            form_Data.append('LON', formData.LON);
            form_Data.append('LAT', formData.LAT);
            form_Data.append('ZIP', formData.ZIP);
            
            console.log(form_Data)
            console.log(formData)
            var predictedPrice = null
            axios.defaults.headers.common["Authorization"] = "";
            axios
                .post("/predictPrice/", form_Data)

                .then((response) => {
                    // this.$router.push("/login");
                    predictedPrice = JSON.parse(response.data)
                    console.log(predictedPrice['PredictedPrice'] ,predictedPrice['PredictedPriceList'],predictedPrice['Weights'])
                    localStorage.setItem('predPrice',predictedPrice['PredictedPrice'])
                    localStorage.setItem('weights',predictedPrice['Weights'])
                    localStorage.setItem('predPriceList',predictedPrice['PredictedPriceList'])
                    localStorage.setItem('buyerSeller',this.buyerSeller)
                    localStorage.setItem('cost',this.cost)
                    this.$router.push("/infopage");

                })
                .catch((error) => {
                    console.log(error);
                });
            setTimeout(this.createCollections(formData),2000)
        },
    },
    components: {}
};
</script>

<style lang="scss" scoped>
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
  text-decoration: none;
  list-style: none;
}

.box {
  width: 80%;
  background: #1d1e22;
  box-shadow: 0px 4px 100px rgba(0, 0, 0, 0.7);
  border-radius: 70px;
  margin: 0 auto;
  overflow: hidden;
  display: flex;
  justify-content: flex-start;
  align-items: flex-start;
  position: relative;
  margin-bottom: 40px;

  .bg-box {
    position: absolute;
    left: 82.36%;
    right: -40.62%;
    top: 51.95%;
    bottom: -33.89%;
    background: rgba(6, 125, 113, 0.3);
    filter: blur(250px);
    // z-index: -1;
  }

  .left-box {
    width: 125px;
    height: 1036px;
    background: #1d1e22;
    box-shadow: 0px 4px 40px rgba(0, 0, 0, 0.3);
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;

    .left-top {
      position: absolute;
      width: 45px;
      height: 45px;
      top: 41px;
      left: 40px;

      img {
        width: 100%;
        height: 100%;
      }
    }

    .left-nav {
      display: flex;
      flex-direction: column;
      align-items: center;

      li {
        width: 50px;
        height: 50px;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 30px;
      }

      li:nth-child(2) {
        margin-bottom: 20px;
      }

      li:nth-child(3) {
        width: 70px;
        height: 70px;
        background-color: #3dbda7;
        border-radius: 50%;
        margin-bottom: 20px;
      }
    }
  }

  .right-box {
    width: 100%;
    margin-left: 35px;
    padding-top: 35px;

    .right-top {
      width: 100%;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-left: 16px;
      padding-right: 41px;

      .search-box {
        width: 473px;
        height: 50px;
        border-radius: 50px;
        display: flex;
        justify-content: flex-start;
        align-items: center;
        padding-left: 31px;
        background: rgba(100, 110, 109, 0.2);
        overflow: hidden;

        input {
          border: none;
          background-color: transparent;
          height: 100%;
          padding-left: 16px;
          width: 423px;
          outline: 0;
          color: #ffffff;
        }

        input:focus {
          border: none;
        }
      }

      .info-box {
        display: flex;
        justify-content: flex-start;
        align-items: center;

        >div {
          width: 55px;
          height: 50px;
          border-radius: 30px;
          display: flex;
          justify-content: center;
          align-items: center;
          background: linear-gradient(180deg, #393939 0%, #1d1e22 100%);

          // overflow: hidden;
          img {
            width: 100%;
            height: 100%;
          }
        }

        .info-pic {
          overflow: hidden;
          cursor: pointer;
        }

        .news {
          margin: 0 19px 0 35px;
          background: #3dbda7;
          position: relative;

          // overflow: auto;
          .dailog-box {
            position: absolute;
            height: 860px;
            width: 334px;
            background: #38393d;
            border-radius: 50px;
            top: 77px;
            right: -74px;
            z-index: 2;
            padding: 0 17px;

            .tit {
              text-align: center;
              font-family: 'Poppins';
              font-style: normal;
              font-weight: 700;
              font-size: 24px;
              line-height: 36px;
              color: #ffffff;
              margin-top: 12px;
            }

            .time-box {
              font-family: 'Poppins';
              font-style: italic;
              font-weight: 300;
              font-size: 16px;
              line-height: 6px;
              color: #ffffff;
              margin-top: 24px;
              margin-left: 15px;
            }

            .item-box1 {
              display: flex;
              justify-content: space-between;
              align-items: center;
              margin-top: 30px;

              .item-left {
                display: flex;
                justify-content: flex-start;
                align-items: flex-start;

                .img-box {
                  width: 64px;
                  height: 64px;
                  border-radius: 15px;
                  overflow: hidden;
                  margin-right: 10px;

                  img {
                    height: 100%;
                    width: 100%;
                  }
                }

                .left-txt {
                  .txt-tit {
                    font-family: 'Poppins';
                    font-style: normal;
                    font-weight: 400;
                    font-size: 16px;
                    line-height: 24px;
                    color: #ffffff;
                  }

                  .txt-sub-tit {
                    font-family: 'Poppins';
                    font-style: normal;
                    font-weight: 500;
                    font-size: 12px;
                    line-height: 18px;
                    color: #969696;
                  }

                  .txt-time {
                    font-family: 'Poppins';
                    font-style: normal;
                    font-weight: 275;
                    font-size: 13px;
                    line-height: 20px;
                    color: #ffffff;
                  }
                }
              }

              .item-right {
                width: 43px;
                height: 40px;
                background: linear-gradient(180deg, #393939 0%, #1d1e22 100%);
                border-radius: 30px;
                display: flex;
                justify-content: center;
                align-items: center;
              }
            }

            .item-box2 {
              width: 300px;
              height: 227px;
              background: #1c2024;
              border-radius: 40px;
              margin-top: 30px;
              padding: 13px 26px 11px 15px;
              margin-bottom: 30px;

              .item2-top {
                display: flex;
                justify-content: space-between;
                align-items: center;
                overflow: hidden;

                .item2-img {
                  width: 62px;
                  height: 62px;
                  border-radius: 50%;
                  overflow: hidden;
                  flex-shrink: 0;

                  img {
                    width: 100%;
                    height: 100%;
                  }
                }

                .txt-tit {
                  h1 {
                    font-family: 'Open Sans';
                    font-style: normal;
                    font-weight: 600;
                    font-size: 24px;
                    line-height: 33px;
                    // text-align: center;
                    color: #ffffff;
                  }

                  h4 {
                    font-family: 'Open Sans';
                    font-style: normal;
                    font-weight: 600;
                    font-size: 14.2385px;
                    line-height: 19px;
                    color: #b9b9b9;
                    margin-top: 15px;
                  }
                }
              }

              p {
                font-family: 'Open Sans';
                font-style: normal;
                font-weight: 700;
                font-size: 12px;
                line-height: 18px;
                letter-spacing: 0.02em;
                color: #ffffff;
                margin-top: 20px;
                padding-right: 20px;
              }
            }

            .item-box3 {
              width: 300px;
              height: 227px;
              background: #1c2024;
              border-radius: 40px;
              overflow: hidden;
              margin: 40px 0;

              img {
                width: 100%;
                height: 100%;
              }
            }
          }
        }
      }
    }

    .right-con {
      width: 850px;
      margin-top: 65px;

      .con-top {
        width: 850px;
        height: 311px;
        border-radius: 50px;
        background: #071b24;
        overflow: hidden;

        img {
          width: 100%;
          height: 100%;
        }
      }

      .box-tit {
        font-family: 'Poppins';
        font-style: normal;
        font-weight: 600;
        font-size: 20px;
        line-height: 20px;
        color: #ffffff;
        margin: 35px 0 35px 11px;
      }

      .con-item-box {
        display: flex;
        justify-content: flex-start;
        flex-wrap: wrap;

        .con-item {
          width: 274px;
          margin-right: 14px;
          cursor: pointer;

          .con-img {
            width: 100%;
            height: 166px;
            border-radius: 30px;
            overflow: hidden;

            img {
              width: 100%;
              height: 100%;
            }
          }

          .sub {
            font-family: 'Inter';
            font-style: normal;
            font-weight: 500;
            font-size: 8px;
            line-height: 11px;
            display: flex;
            align-items: center;
            letter-spacing: 1px;
            text-transform: uppercase;
            color: rgba(245, 245, 245, 0.6);
            margin-top: 9px;
            margin-left: 16px;
          }

          .item-tit {
            font-family: 'Inter';
            font-style: normal;
            font-weight: 600;
            font-size: 10px;
            line-height: 20px;
            display: flex;
            align-items: center;
            letter-spacing: 0.2px;
            color: #f5f5f5;
            margin-left: 16px;
          }

          .item-money {
            font-family: 'Inter';
            font-style: normal;
            font-weight: 400;
            font-size: 14px;
            line-height: 17px;
            display: flex;
            align-items: center;
            letter-spacing: 0.2px;
            color: #f5f5f5;
            margin-left: 16px;
          }
        }

        .con-item:last-child {
          margin-right: 0;
        }
      }
    }
  }
}
</style>
