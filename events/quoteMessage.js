module.exports = {
	name: 'quote',
  on: true,
	execute(client) {
    message =>{
      console.log(`Message found at ${message.channel.name}`);
      if(message.content.includes("https://discord.com/channels/"))
      message.channel.send(message.content)
    }
	},
};
