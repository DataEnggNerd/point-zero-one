# Terminal setup

Being a developer, terminal is one computer application very frequently. I prefer the terminal to be as clean, minimal and as informative as possible. After exploring and using many shells/prompts like [zsh](https://github.com/zsh-users/zsh), [zim](https://github.com/zimfw/zimfw), [ohmyzsh](https://github.com/ohmyzsh/ohmyzsh), [powerlevelk10k](https://github.com/romkatv/powerlevel10k) etcetra, [Fish](https://github.com/fish-shell/fish-shell) and [Startship](https://github.com/starship/starship) made me to settle.

## Fish :fish:

Yes, ZSH is good. But fish attracted me with two very interesting and useful things which zsh doesn't have.

#### Feature one: Autocomplete :dizzy:
The autocomplete feature of fish is the standard for other shells. Trust me, I was amazed to get to know the list of branches in my remote repository just by tapping the :arrow_right: key and this comes just out of the box. To achieve this somewhat similar, you need [zsh autocomplete](https://github.com/marlonrichert/zsh-autocomplete) as a plugin in zsh. Other shells, I really don't wanna know. 

![autocomplete](/docs/assets/fish-autocomplete.png)

#### Feature two: Browser based configuration
I hate to do shell coding and needing to add more and more lines to my [`.zshrc`](https://stackoverflow.com/a/46341026/3488550) file and bloating it up. With adding themes and configurations my `.zshrc` file bloated up so much, I had to reset twice overall. 
Fish handles configuration in a very intuitive way. Type `fish_config`, and press :leftwards_arrow_with_hook: (Enter). Voila :tada:, a nice browser window pop's up which contains A to Z of your fish shell configuration. 
  
![screenshot](/docs/assets/fish-config.png "Browser configuration for fish shell")

#### Beyond the features!
The developers of Fish shell inspired me beyond their tool, through their [design principles](https://fishshell.com/docs/current/design.html). A must read for every software developer, to understand the amount of thought process needed to develop a good piece of software. 

#### Installation and my configuration

To install - `brew install fish`. Simple! 

To make fish as the default shell, `chsh -s /opt/homebrew/bin/fish` and restart your terminal. That's all it take and you can use the `fish_config` to configure everything in a simple way. 

I am using `ayu Dark` theme, which has some nice blue hues throughout. 

## Starship :rocket::crab:
A rust based prompt for any shell, be it zsh, bash, xonsh anything. I stumbled on [`Startship`](https://starship.rs) at trending repositories of github, (yeah, I am bit of a nerd :nerd_face:). Startships selling point to me are the pretty (customisable) icons and configuration, again. 

#### Feature one: ease of configuraion
Starship is written in Rust :crab: and it works based on `toml` based configuration. I would have stopped exploring if it was shell configuration. Startship is not only for developers, but for everyone in my opinion. 
I have attached my configuration [here](my-startship-config.toml) for reference. This makes my prompt look something like this,

![prompt](/docs/assets/starship-prompt.png)

Nice, init :dizzy:!  

#### Feature two: Loaded configuration options
The beauty of starship lies in the versatile list of configurations provided to play around. I would encourage to play around before settling down. Are you a Python developer, you got it, NodeJS developer? you are also [covered](https://starship.rs/config/#node-js). Oh, you work only with AWS? [we got you](https://starship.rs/config/#aws). All of my friends who work in different domain have found their own expertise configuration options here. Even the [Perl](https://starship.rs/config/#perl) developers, I know right :dizzy_face: ?

#### Starship
To install - `brew install startship`, and get into the starship.

Configuration - Visit [configuration page](https://starship.rs/config/) and go nuts.