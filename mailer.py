import os,smtplib,json
  from http.server import HTTPServer,BaseHTTPRequestHandler as BH               
  from email.mime.text import MIMEText
  G=os.environ.get('GMAIL_USER','')
  P=os.environ.get('GMAIL_PASS','')                                             
  T=os.environ.get('TO_EMAIL','')
  class H(BH):                                                                  
   def log_message(s,*a):pass
   def do_OPTIONS(s):
    s.send_response(200)                                                        
    s.send_header('Access-Control-Allow-Origin','*')
    s.send_header('Access-Control-Allow-Headers','Content-Type')                
    s.end_headers()
   def do_POST(s):                                                              
    n=int(s.headers.get('Content-Length',0))
    d=json.loads(s.rfile.read(n))                                               
    try:          
     m=MIMEText('\n'.join(k+': '+str(v)for k,v in d.items()))
     m['From']=G;m['To']=T                                                      
     m['Subject']='Booking: '+d.get('Name','?')
     x=smtplib.SMTP_SSL('smtp.gmail.com',465)                                   
     x.login(G,P);x.send_message(m);x.quit()
     s.send_response(200)                                                       
    except Exception as e:                                                      
     print(e);s.send_response(500)
    s.send_header('Access-Control-Allow-Origin','*')                            
    s.send_header('Content-Type','application/json')
    s.end_headers()                                                             
    s.wfile.write(b'{"ok":true}')
  HTTPServer(('',5000),H).serve_forever()   
