function sum(a,b){
    return a+b;
  }
  
  function square(a){
      return a*a;
  }

  function max(a,b){
      return (a > b) ? a:b;
  }
  
  let globalVar = "Hello from Global!"
  
  function displayGlobal(){
      console.log(globalVar);
  }
  
  function poorLocalVar(){
      let localVar = " i am local ";
      console.log(localVar);
  }
  
  if(true){
      var x = 1;
  }
  console.log(x)
  
  if(true){
      let y = 1;
  }
  console.log(y)
  
  if(true){
      const z = 1;
  }
  console.log(z)
  
  function counter(){
      let count = 0;
  
      return function (){
          count++;
          console.log(count)
      }
  }
  
  const cntr1 = counter();
  const cntr2 = counter();
  
  cntr1();
  cntr1();
  cntr1();
  
  cntr2();
  cntr2();
  cntr2();
  
  
  
  