const { SlashCommandBuilder, roleMention } = require('@discordjs/builders');
const role = roleMention('877902526706499614');
const gamingJSON = require('../jsonData/emote.json');

// admin 291882674564497408
// gaming 877902526706499614

module.exports = {
	data: new SlashCommandBuilder()
		.setName('gaming')
		.setDescription('Notifies the gamers')
		.addStringOption(option => option
			.setName('msg')
			.setDescription('Message to be included')
			.setRequired(false)),
	async execute(interaction) {
		const msg = interaction.options.getString('msg');
		await interaction.reply(gamingJSON.gaming[Math.floor(Math.random() * gamingJSON.gaming.length)]);
		await interaction.channel.send(`${role} ${msg}`);
	},
};
