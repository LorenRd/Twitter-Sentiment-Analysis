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
        <v-col cols="12" sm="6" md="3">
              <v-text-field prepend-inner-icon="mdi-card-text" v-model="text" :rules="[rules.required, rules.counter]"  counter maxlength="250"  label="Paste tweet body"
              ></v-text-field><v-btn @click="getTweetText" color="primary">Analyse!</v-btn>
        </v-col>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
  import * as tf from '@tensorflow/tfjs';
  import axios from "axios";

  export default {
    data(){
      return {
        text: '',
        modelLoaded: false,
        tokenizer: require('../model/tokenizer.json'),
        rules: {
          required: value => !!value || 'Required.',
          counter: value => value.length <= 250 || 'Max 250 characters',
        },
      }
    },
  methods: {
      stringCleaner(text){
        return text.toLowerCase().trim().replace(/@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+/g, " ").split(" ");
      },
      predict(stringCleaned){
        axios.post("http://localhost:5000/predict", {"stringCleaned": stringCleaned})
        .then((result) => 
        console.log(result.data));
      },
      getTweetText(){
        if(this.$refs.form.validate()){
          let stringCleaned = this.stringCleaner(this.text);
          this.predict(stringCleaned);
        }
      }
    }

  }
</script>
