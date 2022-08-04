new Vue({
  el: '#app',
  data () {
    return {
      dialog: false,
      nav: [
        {
          icon: 'home',
          text: 'Home',
          title: 'Back to Home page',
          active: true
        },
        {
          icon: 'info',
          text: 'signin',
          title: 'sign in',
          active: false
        },

        {
          icon: 'email',
          text: 'share',
          title: 'share with us',
          active: false
        },

        {
          icon: 'email',
          text: 'share',
          title: 'uploudS',
          active: false
        },

        {
          icon: 'email',
          text: 'share',
          title: 'see other comments',
          active: false
        }
      ]
      ]
    }
  }
})