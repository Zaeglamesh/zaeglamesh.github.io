import random

digimonList = {
	'Botamon': {
		'Koromon': {
			'Agumon': {
				'Greymon': {
					'MetalGreymon': {
						'WarGreymon',
						 'ZekeGreymon'
					},
					'MetalGreymon Altreous Mode': {
						'BlitzGreymon',
						'Machinedramon'
					}
				},
				'GeoGreymon': {
					'RizeGreymon': {
						'ShineGreymon'
					}
				},
				'Meramon': {
					'SkullMeramon': {
						'Gankoomon',
						'Boltmon'
					},
					'BlueMeramon': {
						'Boltmon'
					}
				}
			}
		}
	},
	'Punimon': {
		'Tsunomon': {
			'Gabumon': {
				'Garurumon': {
					'WereGarurumon': {
						'MetalGarurumon'
					},
					'ShadowWereGarurumon': {
						'BlackMetalGarurumon',
						'BanchoLeomon'
					},
					'WereGarurumon Sagittarius Mode': {
						'CresGarurumon',
						'ZeedGarurumon'
					}
				},
				'AmenoGarurumon': {
					'FallGarurumon': {
						'ShadeGarurumon'
					}
				}
			}
		}
	},
	'Nyokimon': {
		'Yokomon': {
			'Biyomon': {
				'Birdramon': {
					'Garudamon': {
						'Phoenixmon'
					},
					'Garudamon Aruna Mode': {
						'RebornPhoenixmon'
					}
				},
				'Aquilamon': {
					'Garudamon Aruna Mode': {
						'RebornPhoenixmon'
					},
					'Garudamon': {
						'Phoenixmon'
					}
				},
				'Kokatorimon': {
					'Karatenmon': {
						'Kuzuhamon',
						'Kuzuhamon Maid Mode'
					}
				}
			}
		}
	},
	'Pabumon': {
		'Motimon': {
			'Tentomon': {
				'Kabuterimon': {
					'MegaKabuterimon Red': {
						'HerculesKabuterimon',
						'AncientBeetlemon'
					},
					'MegaKabuterimon Blue': {
						'HerculesKabuterimon',
						'AncientBeetlemon'
					}
				},
				'AquaKabuterimon': {
					'StandKabuterimon': {
						'TwilightKabuterimon'
					}
				},
				'Airdramon': {
					'MetalGreymon Virus': {
						'BlitzGreymon'
					}
				},
				'Cyclonemon': {
					'Orochimon': {
						'Nidhoggmon'
					}
				}
			}
		}
	},
	'Yuramon': {
		'Tanemon': {
			'Palmon': {
				'Sunflowmon': {
					'Ajatarmon': {
						'Hydramon'
					},
					'Lilamon': {
						'Lotosmon',
						'Rosemon'
					},
					'Lillymon': {
						'Rosemon',
						'BanchoLillymon',
						'Rafflesimon'
					}
				},
				'Togemon': {
					'Lillymon': {
						'Rosemon',
						'BanchoLillymon',
						'Rafflesimon'
					}
				},
				'IgniTogemon': {
					'HasteTogemon': {
						'MidnightTogemon'
					}
				}
			}
		},
		'Budmon': {
			'Mushroomon': {
				'Woodmon': {
					'Lillymon': {
						'Rosemon',
						'BanchoLillymon',
						'Rafflesimon'
					},
					'Cherrymon': {
						'Puppetmon'
					}
				}
			}
		}
	},
	'Poyomon': {
		'Bukamon': {
			'Gomamon': {
				'Ikkakumon': {
					'Zudomon': {
						'Vikemon',
						'Plesiomon',
						'BanchoZudomon'
					},
					'Zudomon Blitzgulis Mode': {
						'ThorZudomon'
					}
				},
				'Mojyamon': {
					'Piximon': {
						'Jijimon',
						'Ophanimon'
					}
				},
				'Frigimon': {
					'Pandamon': {
						'BanchoLeomon'
					},
					'Sirenmon': {
						'Junomon'
					}
				}
			}
		},
		'Tokomon': {
			'Patamon': {
				'Angemon': {
					'MagnaAngemon': {
						'Seraphimon',
						'Goldramon'
					},
					'MagnaAngemon Divinity Mode':{ 
						'ShadowSeraphimon',
						'BlackSeraphimon'
					},
					'Angewomon': {
						'Ophanimon',
						'Magnadramon',
						'LovelyAngemon'
					}
				},
				'Unimon': {
					'Indramon': {
						'Zhuqiaomon'
					}
				}
			}
		}
	},
	'MetalBotamon': {
		'MetalKoromon': {
			'Hagurumon': {
				'Mechanorimon': {
					'Gigadramon': {
						'Machinedramon'
					}
				},
				'Guardromon': {
					'Andromon': {
						'Machinedramon',
						'HiAndromon'
					}
				}
			},
			'ShadowToyAgumon': {
				'Guardromon': {
					'Andromon': {
						'Machinedramon',
						'HiAndromon'
					}
				}
			},
			'ToyAgumon': {
				'Guardromon': {
					'Andromon': {
						'Machinedramon',
						'HiAndromon'
					}
				},
				'ToyGreymon': {
					'ToyRizeGreymon': {
						'ToyShineGreymon'
					}
				}
			},
			'ClearAgumon': {
				'Guardromon': {
					'Andromon': {
						'Machinedramon',
						'HiAndromon'
					}
				},
				'ToyGreymon': {
					'ToyRizeGreymon': {
						'ToyShineGreymon'
					}
				}
			}
		}
	},
	'Pabumon': {
		'Motimon': {
			'Solarmon': {
				'Meramon': {
					'SkullMeramon':	{
						'Boltmon',
						'Gankoomon'
					}
				},
				'Clockmon': {
					'Andromon': {
						'HiAndromon'
					},
					'Knightmon': {
						'Crusadermon', 
						'Leopardmon',
						'Leopardmon Leopard Mode'
					}
				}
			}
		}
	},
	'Chibomon': {
		'DemiVeemon': {
			'Veemon': {
				'Veedramon': {
					'AeroVeedramon': {
						'UlforceVeedramon'
					}
				},
				'RedVeedramon': {
					'AeroVeedramon': {
						'UlforceVeedramon'
					}
				},
				'BlackVeedramon': {
					'HydroVeedramon': {
						'AlphaVeedramon',
						'WarVeedramon'
					}
				},
				'GoldVeedramon': {
					'HydroVeedramon': {
						'AlphaVeedramon',
						'WarVeedramon'
					}
				}
			}
		}
	},
	'Pururumon': {
		'Poromon': {
			'Hawkmon': {
				'Aquilamon': {
					'Garudamon': {
						'Phoenixmon'
					},
					'Garudamon Aruna Mode': {
						'RebornPhoenixmon'
					}
				},
				'Peckmon': {
					'Sinduramon': {
						'Valdurmon'
					},
					'Crowmon': {
						'Ravemon'
					}
				}
			}
		}
	},
	'Tsubamon': {
		'Upamon': {
			'Armadillomon': {
				'Ankylomon': {
					'Shakkoumon': {
						'Vikemon',
						'SlashAngemon'
					}
				},
				'Tortomon': {
					'Brachiomon': {
						'UltimateBrachiomon'
					}
				}
			}
		}
	},
	'Leafmon': {
		'Minomon': {
			'Wormmon': {
				'Stingmon': {
					'JewelBeemon': {
						'GranKuwagamon',
						'BanchoStingmon'
					}
				},
				'Hudiemon': {
					'JewelBeemon': {
						'GranKuwagamon',
						'BanchoStingmon'
					}
				}
			}
		}
	}
}

freshChoice = random.choice(list(digimonList))
intrainingChoice = random.choice(list(digimonList[freshChoice]))
rookieChoice = random.choice(list(digimonList[freshChoice][intrainingChoice]))
championChoice = random.choice(list(digimonList[freshChoice][intrainingChoice][rookieChoice]))
ultimateChoice = random.choice(list(digimonList[freshChoice][intrainingChoice][rookieChoice][championChoice]))
megaChoice = random.choice(list(digimonList[freshChoice][intrainingChoice][rookieChoice][championChoice][ultimateChoice]))
print(freshChoice, intrainingChoice, rookieChoice, championChoice, ultimateChoice, megaChoice)
#print(numChoice, freshChoice, intrainingChoice)
