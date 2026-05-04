import re
  f = open('/var/www/html/index.html').read()
  new = """function submitBooking(){
  var n=document.getElementById('f-name').value.trim();
  var p=document.getElementById('f-phone').value.trim();
  var t=document.getElementById('f-treatment').value;
  var d=document.getElementById('f-datetime').value;
  var m=document.getElementById('f-message').value.trim();
  if(!n||!p||!t){alert('Fill name, phone and treatment.');return;}
  var b=document.querySelector('.modal-submit');
  b.textContent='Sending...';b.disabled=true;
  var u='http://'+location.hostname+':5000';
  fetch(u,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.s
  tringify({Name:n,Phone:p,Treatment:t,DateTime:d,Message:m})})
  .then(function(r){if(r.ok){alert('Appointment
  received!');closeModal();}else{alert('Error. Call 099255 42424.');}})
  .catch(function(){alert('Error. Call 099255 42424.');})
  .finally(function(){b.textContent='Confirm Appointment
  Request';b.disabled=false;});
  }"""
  f = re.sub(r'function submitBooking\(\)\{.*?closeModal\(\)\s*\}', new, f,
  flags=re.DOTALL)
  open('/var/www/html/index.html','w').write(f)
  print('Done!')
