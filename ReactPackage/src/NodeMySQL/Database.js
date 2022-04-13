const {createPool}=require('mysql')
const pool = createPull({
    host: "",
    user :"",
    password: "",
    connectLimit:10
})

