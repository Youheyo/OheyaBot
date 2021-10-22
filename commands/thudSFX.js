const { SlashCommandBuilder } = require('@discordjs/builders');
const storage = ['https://cdn.discordapp.com/attachments/805871223903879249/899700610050457600/21342343.mp4'];

// admin 291882674564497408
// gaming 877902526706499614

module.exports = {
	data: new SlashCommandBuilder()
		.setName('thudsfx')
		.setDescription('THUD!'),
	async execute(interaction) {

		await interaction.reply(storage[Math.floor(Math.random() * storage.length)]);
	},
};
