const { SlashCommandBuilder, roleMention } = require('@discordjs/builders');
const role = roleMention('877902526706499614');
const gifStorage = require('../jsonData/emote.json');

// admin 291882674564497408
// gaming 877902526706499614

module.exports = {
	data: new SlashCommandBuilder()
		.setName('gaming')
		.setDescription('Notifies the gamers'),
	async execute(interaction) {
		await interaction.reply(gifStorage.gaming[Math.floor(Math.random() * gifStorage.length)]);
		await interaction.channel.send(`${role}`);
	},
};
