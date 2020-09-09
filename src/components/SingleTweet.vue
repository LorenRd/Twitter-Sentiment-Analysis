<template>
  <v-form ref="form" @submit.prevent="getTweetText()" :style="{background: background, height: '100%'}">
    <v-progress-linear v-show="tweetLoading" indeterminate color="cyan" />
    <v-container
      class="fill-height"
      fluid
    >
      <v-row
          align="center"
          justify="center"
        >
      <h1>Text analyser</h1>
      </v-row>
      <v-row
        align="center"
        justify="center"
      >
        <v-col cols="12" sm="6">
              <v-text-field prepend-inner-icon="mdi-card-text" v-model="text" :rules="[rules.required, rules.counter]"  counter maxlength="250"  label="Write some text..."
              ></v-text-field><v-btn :disabled="tweetLoading" type="submit" color="primary">Analyse!</v-btn>
              <v-row
                align="center"
                justify="center"
                style="height: 150px;"
              >
              <span v-show="label !== ''">Score: {{score}} ({{label}})</span>
              </v-row>
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
        text: '',
        score: 0,
        label: '',
        background: '',
        tweetLoading: false,
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
        axios.post("http://127.0.0.1:5000/predict", {"stringCleaned": stringCleaned}, {headers: {"Access-Control-Allow-Origin": "*"}})
        .then((result) => {
          this.score = result.data.score;
          this.label = result.data.label;
          // #E57373 - red , #FFF59D - yellow, #81C784 - green
          if(this.label == 'POSITIVE')
            this.background = '#81C784'
          else if(this.label == 'NEGATIVE')
            this.background = '#E57373'
          else
            this.background = '#FFF59D'
          console.log(result.data)
        });
      },
      getTweetText(){
        if(this.$refs.form.validate()){
          this.tweetLoading = true;
          let stringCleaned = this.stringCleaner(this.text);
          this.predict(stringCleaned);
          this.tweetLoading = false;
        }
      }
    }

  }
</script>
