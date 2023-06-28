css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
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
  color: #fff;
  font-size:1.4rem;
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
        <img src="https://www.mattosfilho.com.br/wp-content/uploads/2022/05/andrea-bazzo-1.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''