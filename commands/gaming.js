const { SlashCommandBuilder, roleMention } = require('@discordjs/builders');
const role = roleMention('877902526706499614');
const storage = require('../jsonData/emote.json');

// admin 291882674564497408
// gaming 877902526706499614

module.exports = {
	data: new SlashCommandBuilder()
		.setName('gaming')
		.setDescription('Notifies the gamers'),
	async execute(interaction) {
		//await interaction.reply(storage.gaming[Math.floor(Math.random() * storage.length)]);
		await interaction.reply(`${role}`);
	},
};
