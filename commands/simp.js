const { SlashCommandBuilder } = require('@discordjs/builders');

const towaS = [
	'https://cdn.discordapp.com/attachments/771384438080274432/870706256539705405/IMG_20210725_233235.jpg',
	'https://cdn.discordapp.com/attachments/771384438080274432/819625731037593630/IMG_20210307_165339.jpg',
	'https://pbs.twimg.com/media/Enaadk9WEAA8IdV?format=jpg&name=large', 'https://twitter.com/k_e_cttp/status/1448512072510164996?s=19',
];

const cleveS = [
	'https://images-ext-1.discordapp.net/external/z-39n8DBIXrFiUiTdXfzYNISA6DUkJhtzNDIlmxA9KY/https/pbs.twimg.com/media/E6_ob65VgAIx8k_.jpg%3Alarge?width=271&height=482',
	'https://pbs.twimg.com/media/E-B7OCSVEAQt_8v.jpg:large',
	'https://cdn.discordapp.com/attachments/771384438080274432/870706256904585216/IMG_20210725_233202.jpg',
];

const honkS = [
	'https://images-ext-2.discordapp.net/external/IL9NKG6UY5bQI9yAgRshtUXnHSfFbdoVI3WxEwPkPLk/https/pbs.twimg.com/media/E72_sS_VcAAhhdR.jpg%3Alarge?width=638&height=482',
	'https://media.discordapp.net/attachments/177862772661551104/871955876783738900/4a567f8f8aabe99ada8ff6db3dd41c48.png?width=293&height=482',
	'https://images-ext-1.discordapp.net/external/rRjb93bqna4bW--JM0IfnnhsKYtmRt0j9O1XSgXoU9U/https/pbs.twimg.com/media/E7y6YZHUcAEHEia.jpg%3Alarge?width=353&height=482',
];


module.exports = {
	data: new SlashCommandBuilder()
		.setName('simp')
		.setDescription('Send an image')
		.addStringOption(option => option.setName('candidate').setDescription('Candidates').setRequired(true)
			.addChoice('towa', 'towa')
			.addChoice('cleve', 'cleve')
			.addChoice('honk', 'honk')
		),
		async execute(interaction){
			//console.log(interaction.options.get('candidate'));
			let storage = [];
			switch(interaction.options.get('candidate').value){
				case 'towa':
					storage = towaS;
					break;
				case 'cleve':
					storage = cleveS;
					break;
				case 'honk':
					storage = honkS;
					break;
			}
			await interaction.reply(storage[Math.floor(Math.random() * storage.length)]);
		},
};
