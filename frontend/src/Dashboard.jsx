import {useEffect,useState}
from "react"


function Dashboard(){

const[
records,
setRecords

]=useState([])


useEffect(()=>{

fetch(
"https://breathe-esg-assignment-en1h.onrender.com/api/records/"
)

.then(
r=>r.json()
)

.then(
d=>setRecords(d)
)

},[])



return(

<div
style={

{

padding:"30px",

fontFamily:"Arial"

}

}
>

<h1>

Breathe ESG Dashboard

</h1>


{

records.map(

r=>

<div

key={r.id}

style={

{

border:

"1px solid gray",

borderRadius:

"10px",

padding:

"20px",

marginBottom:

"20px"

}

}

>

<h2>

{r.source}

</h2>


<p>

Category:

{r.category}

</p>


<p>

Value:

{r.value}

</p>


<p>

Unit:

{r.unit}

</p>


<p>

Approved:

{

r.approved

?

"✅"

:

"❌"

}

</p>

</div>

)

}

</div>

)

}

export default Dashboard