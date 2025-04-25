# Pokebot Stadium <a href="https://pokeapi.co/api/v2/pokemon/wooper"><img src='https://veekun.com/dex/media/pokemon/global-link/194.png' height=50px/></a>

A python based Discord bot created with the wrapper for [PokéAPI](https://pokeapi.co). (former [pykemon](https://github.com/PokeAPI/pokepy/tree/bb72105f4c5402aaa5d4fd2b9c142bf9b678b254)). This bot displays fun facts and key
information about randomly generated Pokemon. Enjoy!

## <img src='https://veekun.com/dex/media/pokemon/icons/194.png' height=35px> Installation
Simply click on the link to add the bot to your list of Discord Apps or your own Personal / Public Server!
### <a href="https://discord.com/oauth2/authorize?client_id=1365402539423694848">Click Here to Install the Bot</a>

## <img src='https://veekun.com/dex/media/pokemon/icons/194.png' height=35px> Dependencies

Active Discord Account required. Once available go to https://discord.com/developers/applications to create your first bot application then retrieve the Discord Bot Token. 
This is required to run the Bot via your preferred IDE ( VS Code, Pycharm, etc.)


```sh
$ pip install discord
```

```sh
$ pip install python_dotenv
```
```sh
$ pip install pokepy
```

## <img src='https://veekun.com/dex/media/pokemon/icons/195.png' height=35px> Usage

Even simpler:

```python
>>> import pokepy
>>> client = pokepy.V2Client()
>>> client.get_pokemon(14)
<Pokemon - Kakuna>
```

## <img src='https://veekun.com/dex/media/pokemon/icons/194.png' height=35px>  Documentation

This project utilizes the Pokemon API at https://pokeapi.co/

Pokemon Images were pulled and referenced from the global JSON repo at https://veekun.com/dex/media/pokemon/global-link/

The Python Wrapper, PokePy, had been utilized to build this discord bot. 
For more information, check the documentation at https://pokeapi.github.io/pokepy

## <img src='https://veekun.com/dex/media/pokemon/icons/195.png' height=35px> Features

* User Friendly
* Available for Any Servers
* Minimally invasive due to minimal permissions needed

Inherited from PokePY
* Generate Python objects from PokéAPI resources
* Cache
* Human-friendly API

## Douglas, the Quagsire Certfied 👍<img src='https://veekun.com/dex/media/pokemon/icons/195.png' height=35px>