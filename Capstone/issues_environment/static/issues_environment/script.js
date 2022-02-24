
const App = {
    delimiters: ['[[', ']]'],
    el: '#app',
    data() {
        return {
            message: 'Testing!!!',
            searchEntry: '',
            searchResult: '',
            countryIssueInfo: [
                {
                    name: 'example',
                    issues: ['united states']
                }
            ],
            csrfmiddlewaretoken: ''

        }
    },
    created() { // created hook runs when vue app is created
        // this.getInfo()
    },
    mounted () { // mounted hook runs when html is loaded
        this.csrfmiddlewaretoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value
        // console.log(this.csrfmiddlewaretoken)
    },
    methods: {
        getInfo() {

            axios({
                method: 'post',
                url: '/country_issue_info',
                data: {'searchEntry' : this.searchEntry},
                headers: {
                    'X-CSRFToken': this.csrfmiddlewaretoken
                }
            })
                .then(res => {
                    console.log(res)
                    console.log(res.data)
                    console.log(res.data.countries)
                    this.countryIssueInfo = res.data.countries
                    // this.searchResult.push(res.data)
                    // console.log(this.searchResult)
                })
        }

    },
}

Vue.createApp(App).mount('#app')



            // need to use searchEntry to get data from table? 
            //save first then GET?
            // this.itemsToDo.push(this.searchEntry)
            // print('')}