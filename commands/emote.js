const { SlashCommandBuilder } = require('@discordjs/builders');

const emoteJSON = require('../jsonData/emote.json');


// admin 291882674564497408
// gaming 877902526706499614

module.exports = {
	data: new SlashCommandBuilder()
		.setName('emote')
		.setDescription('Send an emote')

			.addSubcommand(subcommand =>
				subcommand
				.setName('image')
				.setDescription('Send Image Emote')
				.addStringOption(option =>
					option.setName('emotes')
					.setDescription('Choose an Image emote')
					.setRequired(true)
						.addChoice('pain', 'pain')
						.addChoice('man', 'man')
					)
			)
			.addSubcommand(subcommand => subcommand
				.setName('video')
				.setDescription('Send Video Emote')
				.addStringOption(option =>
					option.setName('emotes')
					.setDescription('Choose a Video emote')
					.setRequired(true)
						.addChoice('cringe' , 'cringe')
						.addChoice('sad', 'sad')
					)
			)
			.addSubcommand(subcommand => subcommand
				.setName('gif')
				.setDescription('Send Gif Emote')
				.addStringOption(option =>
					option.setName('emotes')
					.setDescription('Choose a Gif emote')
					.setRequired(true)
						.addChoice('unravel' , 'unravel')
					)
			),
	async execute(interaction) {
		let storage = [];
		switch(interaction.options.getSubcommand()){
			case 'image':
				switch(interaction.options.get('emotes').value){
					case 'pain' : storage = emoteJSON.image.pain;break;
					case 'man' : storage = emoteJSON.image.man;break;
				}
				break;

			case 'video':
			switch(interaction.options.get('emotes').value){
				case 'cringe' : storage = storage = emoteJSON.video.cringe;break;
				case 'sad' : storage = storage = emoteJSON.video.sad;break;
			}
				break;
			case 'gif':
			switch(interaction.options.get('emotes').value){
				case 'unravel' : storage = emoteJSON.gif.unravel;break;
			}
				break;
			default:
				console.log('Emote does not exist');
				return;
		}
		await interaction.reply(storage[Math.floor(Math.random() * storage.length)]);
	},
};
