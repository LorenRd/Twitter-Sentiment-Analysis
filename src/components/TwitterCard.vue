  <template>
    
  <v-card
    class="mt-5 mx-auto"
    :color="setColor()"
    width="400"
  >
    <v-card-title>
    </v-card-title>

    <v-card-text class="headline font-weight-bold">
      {{tweetBody}}
    </v-card-text>

    <v-card-actions>
      <v-list-item class="grow">
        <v-list-item-avatar color="grey darken-3">
          <v-img
            class="elevation-6"
            :src="userProfile"
          ></v-img>
        </v-list-item-avatar>

        <v-list-item-content>
          <v-list-item-title>{{username}}</v-list-item-title>
        </v-list-item-content>

        <v-row
          align="center"
          justify="end"
        >
          <span class="subheading mr-2">Score: {{score}}</span>
        </v-row>
      </v-list-item>
    </v-card-actions>
  </v-card>
</template>
<script>
  export default {

    data(){
      return{
        color: '',
      }
    },
    props: ['tweetBody', 'score', 'username', 'userProfile', 'label'],
    methods: {
      setColor(){
        // #E57373 - red , #FFF59D - yellow, #81C784 - green
        let color = '';
        if(this.label == 'POSITIVE'){
          color = '#81C784'
        }
        else if (this.label == 'NEGATIVE'){
          color = '#E57373'
        }else{
          color = '#FFF59D'
        }
        return color;
      }
    }
  }
</script>