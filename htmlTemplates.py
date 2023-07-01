css = '''
<style>
body{
    background-color: red !important;
}

.css-1m1kki9, .css-1k35nym, .css-f2nqe9, .css-n5k75g, .css-4z1n4 {
  display:none !important;
}

img, .css-10trblm{
 mouseevent:none;
  
}
.chat-message {
    padding: 1.5rem; 
  border-radius: 0.5rem; 
  margin-bottom: 1rem; 
  display: flex;
  
}
.chat-message.user {
    background-color: #2a303c;
  color: #ccc;
  cursor: help;
      
}
.chat-message.bot {
    background-color: #475063;
  color: #fff;
  cursor:crosshair;
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  font-size:1.2rem;
}
.chat-message.bot:hover{
color:lightgreen;
filter: drop-shadow(16px 16px 20px red) invert(85%);
}

.chat-message.user:hover{
color:lightblue;
}

.css-cio0dv, .css-eh5xgm{
    display:none;
}

'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://media2.giphy.com/media/l2JIireYxichTAGpq/giphy.gif?cid=ecf05e4742fyaf4sou6ohjj0i3xlgh5ejsb7l2a0mprm4okh&ep=v1_gifs_search&rid=giphy.gif&ct=g">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="http://cybersamurai.co.uk/assets/images/profileAi/profileAi%20(23).jpg">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
