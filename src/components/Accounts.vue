<template>
  <v-form ref="form">
    <v-container
      class="fill-height"
      fluid
    >
    <v-row
        align="center"
        justify="center"
      >
      <h2>Account analyser</h2>
          </v-row>
      <v-row
        align="center"
        justify="center"
      >
        <v-col cols="12" sm="6" md="3">
              <v-text-field prepend-inner-icon="mdi-account" v-model="username" :rules="[rules.required]"  label="@username"
              ></v-text-field><v-btn @click="getTweetText" color="primary">Search!</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
  import axios from "axios";

  export default {
    data(){
      return {
        username: '',
        rules: {
          required: value => !!value || 'Required.',
        },
      }
    },
  methods: {
      searchUsername(username){
        axios.post("https://nlp-sentiment-analysis-backend.herokuapp.com/predict", {"username": username}, {headers: {"Access-Control-Allow-Origin": "*"}})
        .then((result) => 
        console.log(result.data));
      },
      getTweetText(){
        if(this.$refs.form.validate()){
          let usernameInfo = this.searchUsername(this.username);
            console.log(usernameInfo)
        }
      }
    }

  }
</script>
