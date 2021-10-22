const { SlashCommandBuilder } = require('@discordjs/builders');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('info')
		.setDescription('Gets info on user or server')
		.addSubcommand(subcommand =>
			subcommand
				.setName('user')
				.setDescription('Info about a user')
				.addUserOption(option => option.setName('target').setDescription('The user').setRequired(true)))
		.addSubcommand(subcommand =>
			subcommand
				.setName('server')
				.setDescription('Info about the server')),
		async execute(interaction){
			switch(interaction.options.getSubcommand()){
				case 'user':
				{
					//console.log(interaction.options.get('target').user.id);
					const person = interaction.options.get('target');
					/*await interaction.reply(`Your tag: ${interaction.get('target').user.tag}\nUser id: ${interaction.options.get('target').user.id}`);*/
					await interaction.reply(`Your tag: ${person.user.tag}\nUser id: ${person.user.id}`);
					break;
				}
				case 'server':
					await interaction.reply(`Server name: ${interaction.guild.name}\nTotal members: ${interaction.guild.memberCount}`);
					break;
				default:
			}
		},
};
