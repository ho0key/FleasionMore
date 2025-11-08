import sys
from colorama import Fore, Style, init
init()
import os
import json

# user guide for making your own
# addon/addon2 will set replacee/replacement to a string. addon can be a list (optional), addon2 cant
# start_key/start_key2 will start the user in a json from a set position (make sure the set position doesnt share a name or ill go to the first one)
# return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names finishes an area and returns all the data back and finishes this codes use
# add a line push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names) for doing multiple changes of seperate things in the same case
# if you want to skip then set skip to True
# leaving empty and only returning will make the user enter 2 from the json starting from the top

def get_valid_input(prompt, valid_values=None):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == 'back':
            return 'back'
        try:
            if valid_values is None or int(user_input) in valid_values:
                return int(user_input)
            else:
                print(f"{Fore.RED}\nInvalid option. Please choose from {valid_values}.\n{Style.RESET_ALL}")
        except ValueError:
            print(f"{Fore.RED}\nInvalid input. Please enter a valid number.\n{Style.RESET_ALL}")


def push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names):
    main_module = sys.modules['__main__']
    main_module.backbone(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)



def bootstrapper():
    base_path = os.path.join(os.getenv('LOCALAPPDATA'), bootstrapper_type, 'Modifications')
    nested_folders = ["PlatformContent", "pc", "textures", "sky"]

    if not os.path.exists(base_path):
        print(f"{Fore.RED}{bootstrapper_type} not found{Style.RESET_ALL}")
    else:
        path = base_path
        for folder in nested_folders:
            path = os.path.join(path, folder)
            if not os.path.exists(path):
                os.makedirs(path)
                print(f"Created folder: {path}")
            else:
                print(f"Folder already exists: {path}")

        print("All folders created successfully! Import your skyboxes into the opened folder.")
        os.startfile(path)

def run(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names):

    while True:
        options = get_valid_input(
                        f"{Fore.MAGENTA}Discord: ho0key{Style.RESET_ALL}\n"
                        f"Asset replacements:\n"
                        f"0:  {Fore.LIGHTMAGENTA_EX}Custom{Style.RESET_ALL}\n"
                        f"1:  {Fore.LIGHTMAGENTA_EX}Sights{Style.RESET_ALL}\n"
                        f"2:  {Fore.LIGHTMAGENTA_EX}Arm model tweaks{Style.RESET_ALL}\n"
                        f"3:  {Fore.LIGHTMAGENTA_EX}Sleeves{Style.RESET_ALL}\n"
                        f"4:  {Fore.LIGHTMAGENTA_EX}No textures{Style.RESET_ALL}\n"
                        f"5:  {Fore.LIGHTMAGENTA_EX}Default skyboxes{Style.RESET_ALL}\n"
                        f"6:  {Fore.LIGHTMAGENTA_EX}Gun skins TEMPORARILY DEPRECATED{Style.RESET_ALL}\n"
                        f"7:  {Fore.LIGHTMAGENTA_EX}Gun Sounds{Style.RESET_ALL}\n"
                        f"8:  {Fore.LIGHTMAGENTA_EX}Gun smoke{Style.RESET_ALL}\n"
                        f"9:  {Fore.LIGHTMAGENTA_EX}Hit tweaks{Style.RESET_ALL}\n"
                        f"10: {Fore.LIGHTMAGENTA_EX}Grenade tweaks{Style.RESET_ALL}\n"
                        f"11: {Fore.LIGHTMAGENTA_EX}Misc tweaks{Style.RESET_ALL}\n"
                        f"12: {Fore.LIGHTMAGENTA_EX}Grenade Warning{Style.RESET_ALL}\n"
                        f"13: {Fore.LIGHTMAGENTA_EX}Ho0keys tweaks{Style.RESET_ALL}\n"
                        f"14: {Fore.LIGHTMAGENTA_EX}Texture packs(NEW!!){Style.RESET_ALL}\n"
                        f"{Fore.CYAN}</> : Lisdex<3 {Style.RESET_ALL}\n"
                        f"Type 'back' to return to the previous menu.\n: ",
                        valid_values=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        )
        if options == 'back':
            print(f"{Fore.CYAN}\nReturning to main menu.{Style.RESET_ALL}")
            skip = True
            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names

        try:
            match options:
                case 0:
                    return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                case 1:
                    while True:
                        sight_option = get_valid_input(
                            f"\nEnter sight option:\n"
                            f"1: {Fore.LIGHTMAGENTA_EX}Reticle tweaks{Style.RESET_ALL}\n"
                            f"2: {Fore.LIGHTMAGENTA_EX}Sight model tweaks{Style.RESET_ALL}\n"
                            f"3: {Fore.LIGHTMAGENTA_EX}Ballistics tracker image tweaks{Style.RESET_ALL}\n"
                            f"4: {Fore.LIGHTMAGENTA_EX}Anti sight tweak{Style.RESET_ALL}\n"
                            f"5: {Fore.LIGHTMAGENTA_EX}Remove Ballistics tracker{Style.RESET_ALL}\n"
                            f"Type 'back' to return to the previous menu.\n: ",
                            valid_values=[1, 2, 3, 4, 5]
                        )
                        if sight_option == 'back':
                            print(f"{Fore.CYAN}\nReturning to Asset replacements.\n{Style.RESET_ALL}")
                            break

                        match sight_option:
                            case 1:
                                start_key = "reticles"
                                start_key2 = "reticle replacement"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 2:
                                while True:
                                    sightbackground = get_valid_input(
                                        f"\nEnter background tweak:\n"
                                        f"1: {Fore.LIGHTMAGENTA_EX}clear coyote blue background{Style.RESET_ALL}\n"
                                        f"2: {Fore.LIGHTMAGENTA_EX}clear reflex blue background{Style.RESET_ALL}\n"
                                        f"3: {Fore.LIGHTMAGENTA_EX}clear okp-7 blue background{Style.RESET_ALL}\n"
                                        f"4: {Fore.LIGHTMAGENTA_EX}clear black ring{Style.RESET_ALL}\n"
                                        f"5: {Fore.LIGHTMAGENTA_EX}remove sniper black circle{Style.RESET_ALL}\n"
                                        f"6: {Fore.LIGHTMAGENTA_EX}remove glass hack border{Style.RESET_ALL}\n"
                                        f"7: {Fore.LIGHTMAGENTA_EX}make oled good{Style.RESET_ALL}\n"
                                        f"8: {Fore.LIGHTMAGENTA_EX}Remove Kosaku (ho0key){Style.RESET_ALL}\n"
                                        f"9: {Fore.LIGHTMAGENTA_EX}Remove Kosaku white dots (ho0key){Style.RESET_ALL}\n"
                                        f"10: {Fore.LIGHTMAGENTA_EX}Invis z-point (ho0key){Style.RESET_ALL}\n"
                                        f"Type 'back' to return to the previous menu.\n: ",
                                        valid_values=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
                                    )
                                    if sightbackground == 'back':
                                        print(f"{Fore.CYAN}\nReturning to sight options.{Style.RESET_ALL}")
                                        break

                                    match sightbackground:
                                        case 1:
                                            addon = "3fc9141fc7c1167c575b9361a98f04c0"
                                            addon2 = "5873cfba79134ecfec6658f559d8f320"
                                            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                                        case 2:
                                            addon = "2eaae4fe3a9fce967af993d27ad68d52"
                                            addon2 = "5873cfba79134ecfec6658f559d8f320"
                                            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                                        case 3:
                                            addon = "2eaae4fe3a9fce967af993d27ad68d52"
                                            addon2 = "5873cfba79134ecfec6658f559d8f320"
                                            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                                        case 4:
                                            addon = "7d5652167ec33ed349e569a55a398705"
                                            addon2 = "75205be5a167842c7ed931d9d5a904ca"
                                            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                                        case 5:
                                            addon = ["a883a2373ad6931556dce946c50c3690", "5a2a41b0da7ec98bf25780bb3f5d071f"]
                                            addon2 = "75205be5a167842c7ed931d9d5a904ca"
                                            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                                        case 6:
                                            addon = '71718d43e373e3633f4ff3b70ec19cf7'
                                            addon2 = 'GH_Black_Border'
                                            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                                        case 7:
                                            addon = '0f621cf9866d643421f0292a85f9be98'
                                            addon2 = 'b99ee82264ed6bfdd815f2f568abff3a'
                                            push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                            addon = '0fd98b21b47dbd948988ec1c67696af8'
                                            addon2 = '5873cfba79134ecfec6658f559d8f320'
                                            push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                            addon = '009b0b998ae084f23e5c0d7b1f9431b3'
                                            addon2 = '577f6c95249ebea2926892c3f3e8c040'
                                            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                                        case 8:
                                            addon = '0ba25a5e810da83a31db384ade65aad2'
                                            addon2 = '5873cfba79134ecfec6658f559d8f320'
                                            push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                            addon = '9e80aa02a7c57dc9a08ee6768bcfbc8f'
                                            addon2 = '5873cfba79134ecfec6658f559d8f320'
                                            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                                        case 9:
                                            addon = '2d41ab1e5a2d3cdbf0e1856a5274e4e8'
                                            addon2 = '5873cfba79134ecfec6658f559d8f320'
                                            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                                        case 10:
                                            addon = '99c0b33c613f8e56c8119dd7c209d3bf'
                                            addon2 = '5873cfba79134ecfec6658f559d8f320'
                                            push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                            addon = 'c00ac887859d6148d9407504027c5887'
                                            addon2 = '5873cfba79134ecfec6658f559d8f320'
                                            push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                            addon = 'e747707db31e1f0ba45209320e7d7a59'
                                            addon2 = '5873cfba79134ecfec6658f559d8f320'
                                            push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                            addon = '8a9dfbb7544317be401c5e6d37bcc6d5'
                                            addon2 = '5873cfba79134ecfec6658f559d8f320'
                                            push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                            addon = 'd0e41757dcf01feefb9a2bdae29090a0'
                                            addon2 = '5873cfba79134ecfec6658f559d8f320'
                                            push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                            addon = 'ee1195ce41d6f7013e002fd4beb42208'
                                            addon2 = '5873cfba79134ecfec6658f559d8f320'
                                            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names

                            case 3:
                                addon = "66a3dd9c1d934ad0ffb5d45729c44250"
                                start_key2 = "ballistics tracker"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 4:
                                addon = "4d452b49c0416950de7d8c8a248e0c85"
                                start_key2 = "anti"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 5:
                                addon = ["433b362c5173b3bce71aa9533630effa", "2484e8dfa3b145a1429205d74f4ea4d5", "b8e4e06abb02731ad7e034f8dee60f3a", "d668894e3a84fa5d44053679e1f7c29d", "e2fc2f0cd0779d9557adc788a5d9427b"]
                                addon2 = '5873cfba79134ecfec6658f559d8f320'
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names

                case 2:
                    while True:
                        arm_option = get_valid_input(
                            f"\nEnter arm option:\n"
                            f"1: {Fore.GREEN}Remove options{Style.RESET_ALL}\n"
                            f"2: {Fore.GREEN}Reflective sleeves{Style.RESET_ALL}\n"
                            f"3: {Fore.GREEN}Bone arms{Style.RESET_ALL}\n"
                            f"4: {Fore.GREEN}Cooler arms{Style.RESET_ALL}\n"
                            f"Type 'back' to return to the previous menu.\n: ",
                            valid_values=[1, 2, 3, 4]
                        )

                        if arm_option == 'back':
                            print(f"{Fore.CYAN}\nReturning to Asset replacements.\n{Style.RESET_ALL}")
                            break

                        match arm_option:
                            case 1:
                                start_key = "arm models"
                                addon2 = "5873cfba79134ecfec6658f559d8f320"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 2:
                                addon = ["ac95c4dbcb1a5ec120bc64b369d41fc3", "da00c2a2bba51d962b29423c25b28bd3", "60a99d5ab2dbf24f654b93b731f720c7", "6e649a3ad144c63298bafb5f0583ed7d"]
                                start_key2 = "remove"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 3:
                                while True:
                                    bone_arm_option = get_valid_input(
                                        f"\nEnter arm option:\n"
                                        f"1: {Fore.GREEN}Left Arms{Style.RESET_ALL}\n"
                                        f"2: {Fore.GREEN}Right Arms{Style.RESET_ALL}\n"
                                        f"Type 'back' to return to the previous menu.\n: ",
                                        valid_values=[1, 2]
                                    )

                                    if bone_arm_option == 'back':
                                        print(f"{Fore.CYAN}\nReturning to Arm Options.\n{Style.RESET_ALL}")
                                        break

                                    match bone_arm_option:
                                        case 1:
                                            while True:
                                                lbone_arm_option = get_valid_input(
                                                    f"\nEnter arm option:\n"
                                                    f"1: {Fore.GREEN}Left Bone{Style.RESET_ALL}\n"
                                                    f"2: {Fore.GREEN}Left Sleeve{Style.RESET_ALL}\n"
                                                    f"Type 'back' to return to the previous menu.\n: ",
                                                    valid_values=[1, 2]
                                                )

                                                if lbone_arm_option == 'back':
                                                    print(f"{Fore.CYAN}\nReturning to Bone Arm Options.\n{Style.RESET_ALL}")
                                                    break

                                                match lbone_arm_option:
                                                    case 1:
                                                        addon = "c0975ad2729339e86a60acac5e5d5867"
                                                        addon2 = "aa453084baf61e05bb0b761511f8b80a"
                                                        return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                                                    case 2:
                                                        addon = "ff874e07a882070ea5cb0c3369e4d269"
                                                        addon2 = "92592c4baca15cecf4dd5bbe2b36e7f2"
                                                        return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                                        case 2:
                                            while True:
                                                rbone_arm_option = get_valid_input(
                                                    f"\nEnter arm option:\n"
                                                    f"1: {Fore.GREEN}Right Bone{Style.RESET_ALL}\n"
                                                    f"2: {Fore.GREEN}Right Sleeve{Style.RESET_ALL}\n"
                                                    f"Type 'back' to return to the previous menu.\n: ",
                                                    valid_values=[1, 2]
                                                )

                                                if rbone_arm_option == 'back':
                                                    print(f"{Fore.CYAN}\nReturning to Bone Arm Options.\n{Style.RESET_ALL}")
                                                    break

                                                match rbone_arm_option:
                                                    case 1:
                                                        addon = "b1c7ea393774f19f9ed47f21e453a0f2"
                                                        addon2 = "257dc7573ff26a51dc732eba6e0e0082"
                                                        return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                                                    case 2:
                                                        addon = "ce07937636c1d66eb9db095dd0098b37"
                                                        addon2 = "feb772c183ba7cd5526e344b258980a6"
                                                        return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 4:
                                addon = ["c0975ad2729339e86a60acac5e5d5867", "eb7d542844ec8de99dbf63a2259b6dc9", "c10c9f476fa22a56b840b540807d2f89", "0929fa96e057727f17934aadd5a18654", "f271a6006decc23bf95a7eedef909e94", "1ae474d121bdf012593d22e7bd5e9854", "19ece9db762c10026a64e078c6eaf735", "fe0ea6c9a2f560fdc7005c3c02c71dce", "4531929c30a509d6a16e655cdd918af9", "0c6deb1bc158cc099db53ac300d952a7", "b8f898ff9aadaee800d07054ef91a769", "6ace0cd56ca5e293a9f87d9b652f7690", "369bdc60330f0dd596a0ee281b12c5c9", "9483c5b01fbaaa6bcc97060d0cb0402f", "f8e86703186511d89859e2b63d169989", "3ebdcfc63270d66a6594028c278913b5", "effba77eb3c7df2880f456ad147e1e7d", "7f88cccd1130e907b7ee96f2b90555ad", "b35db36d16e3ac477de529c1908621a0", "b1c7ea393774f19f9ed47f21e453a0f2", "cfd0d20b94d7e7ced1a18aa270410d50", "85fad2384eb1fcbaf4ccebc2c8d7c84d", "48b7e16ffb6d1ca71bd21a47234d0bbc", "c314fa6eb570bda8e19619e3c1d9d2b7", "7d2d09489b90c07e07f0dc923f118f61", "fe0ea6c9a2f560fdc7005c3c02c71dce"]
                                addon2 = '5873cfba79134ecfec6658f559d8f320'
                                push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                addon = ["ce07937636c1d66eb9db095dd0098b37", "ff874e07a882070ea5cb0c3369e4d269"]
                                addon2 = "8ff6e81c7227fb41f572aef5e9ce5bfc"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                case 3:
                    addon = "ac95c4dbcb1a5ec120bc64b369d41fc3"
                    start_key2 = "skins"
                    return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                case 4:
                    start_key = "textures"
                    addon2 = "75205be5a167842c7ed931d9d5a904ca"
                    return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                case 5:
                    while True:
                        sky_option = get_valid_input(
                            f"\nIs {bootstrapper_type} sky folder setup?\n"
                            f"1: {Fore.GREEN}yes{Style.RESET_ALL}\n"
                            f"2: {Fore.GREEN}no{Style.RESET_ALL}\n"
                            f"Type 'back' to return to the previous menu.\n: ",
                            valid_values=[1, 2]
                        )

                        if sky_option == 'back':
                            print(f"\n{Fore.CYAN}\nReturning to Asset replacements.{Style.RESET_ALL}")
                            break

                        match sky_option:
                            case 1:
                                start_key = "skyboxes"
                                addon2 = "75205be5a167842c7ed931d9d5a904ca"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 2:
                                bootstrapper()
                                start_key = "skyboxes"
                                addon2 = "75205be5a167842c7ed931d9d5a904ca"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                case 6:
                    start_key = "gun skins"
                    start_key2 = "skins"
                    return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                case 7:
                    start_key = "gun sounds"
                    start_key2 = "replacement sounds"
                    return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                case 8:
                    addon = "602e49f80440cdb859fab7182ea4bb23"
                    start_key2 = "gun smoke"
                    return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                case 9:
                    while True:
                        hit_option = get_valid_input(
                            f"\nEnter hit option:\n"
                            f"1: {Fore.LIGHTMAGENTA_EX}Hitmarkers{Style.RESET_ALL}\n"
                            f"2: {Fore.LIGHTMAGENTA_EX}Hit sounds{Style.RESET_ALL}\n"
                            f"3: {Fore.LIGHTMAGENTA_EX}Kill sounds{Style.RESET_ALL}\n"
                            f"4: {Fore.LIGHTMAGENTA_EX}More hitmarkers{Style.RESET_ALL}\n"

                            f"Type 'back' to return to the previous menu.\n: ",
                            valid_values=[1, 2, 3, 4]
                        )
                        if hit_option == 'back':
                            print(f"{Fore.CYAN}\nReturning to Asset replacements.{Style.RESET_ALL}")
                            break

                        match hit_option:
                            case 1:
                                addon = "097165b476243d2095ef0a256320b06a"
                                start_key2 = "hitmarker"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 2:
                                addon = "a177d2c00abd3e550b873d76c97ad960"
                                start_key2 = "replacement sounds"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 3:
                                start_key = "kill default"
                                start_key2 = "replacement sounds"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 4:
                                addon = "097165b476243d2095ef0a256320b06a"
                                start_key2 = "ctmhitmarker"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                case 10:
                    while True:
                        grenade_option = get_valid_input(
                            f"\nEnter grenade option:\n"
                            f"1: {Fore.GREEN}Model tweaks{Style.RESET_ALL}\n"
                            f"2: {Fore.GREEN}Explosion sound{Style.RESET_ALL}\n"
                            f"3: {Fore.GREEN}Grenade sound{Style.RESET_ALL}\n"
                            f"Type 'back' to return to the previous menu.\n: ",
                            valid_values=[1, 2, 3]
                        )
                        if grenade_option == 'back':
                            print(f"{Fore.CYAN}\nReturning to Asset replacements.{Style.RESET_ALL}")
                            break

                        match grenade_option:
                            case 1:
                                while True:
                                    grenade_model_option = get_valid_input(
                                        f"\nEnter model option:\n"
                                        f"1: {Fore.GREEN}RGD{Style.RESET_ALL}\n"
                                        f"2: {Fore.GREEN}Bundle{Style.RESET_ALL}\n"
                                        f"Type 'back' to return to the previous menu.\n: ",
                                        valid_values=[1, 2]
                                    )

                                    if grenade_model_option == 'back':
                                        print(f"{Fore.CYAN}\nReturning to Asset replacements.{Style.RESET_ALL}")
                                        break

                                    match grenade_model_option:
                                        case 1:
                                            start_key = "rgd main"
                                            addon2 = "5873cfba79134ecfec6658f559d8f320"
                                            push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                            start_key = "rgd junk"
                                            start_key2 = "grenades"
                                            push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                            start_key = "rgd texture"
                                            start_key2 = "grenades"
                                            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                                        case 2:
                                            start_key = "bundle main"
                                            addon2 = "5873cfba79134ecfec6658f559d8f320"
                                            push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                            start_key = "bundle junk"
                                            start_key2 = "grenades"
                                            push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                            start_key = "bundle texture"
                                            start_key2 = "grenades"
                                            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 2:
                                start_key = "explosions default"
                                start_key2 = "replacement sounds"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 3:
                                start_key = "grenade sound"
                                start_key2 = "replacement sounds"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                case 11:
                    while True:
                        misc_option = get_valid_input(
                            f"\nEnter misc option:\n"
                            f"1: {Fore.GREEN}M21 Garand Ping{Style.RESET_ALL}\n"
                            f"2: {Fore.GREEN}BFG Machina Sounds{Style.RESET_ALL}\n"
                            f"3: {Fore.GREEN}Damage Affect Tweaks{Style.RESET_ALL}\n"
                            f"4: {Fore.GREEN}Remove Flashlight Beam{Style.RESET_ALL}\n"
                            f"5: {Fore.GREEN}Remove Bullet Casing Sounds{Style.RESET_ALL}\n"
                            f"Type 'back' to return to the previous menu.\n: ",
                            valid_values=[1, 2, 3, 4, 5]
                        )

                        if misc_option == 'back':
                            print(f"{Fore.CYAN}\nReturning to Asset replacements.\n{Style.RESET_ALL}")
                            break

                        match misc_option:
                            case 1:
                                addon = ["07fe5c19cdd350a4922412d00d567edd", "17bb7bd20bf6e1b41214619d16698ff4", "b36ed668aea77715747e3ebadce8a439", "fbc5302726777295ae2ccd092d2748f9"]
                                addon2 = "5873cfba79134ecfec6658f559d8f320"
                                push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                addon = "877cb2de0924e058860135f72e800aad"
                                addon2 = "9296d1de6b6a994aee0f95c1f5206b58"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 2:
                                addon = "9d1808db108b86ddaeda18968a23a804"
                                addon2 = "1689699496f4cf0e2f0fade63f68b83a"
                                push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                addon = ["3ad4ddcb4c77ab8bdfc83cf9c0cfafa9", "edf091bb925fa87900910e501da97018", "768131a75f0d2d95e6799a0a5acd67c6", "3d92b91e96ef916b6717a53ef3f3a442", "32e321c27457289889ac0d5fa72f7d97"]
                                addon2 = "5873cfba79134ecfec6658f559d8f320"
                                push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                addon = "160883329152d9abc5434a1b0982ec7d"
                                addon2 = "0d05028f1eaeb0b97ecd0c473b484371"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 3:
                                while True:
                                    damage_option = get_valid_input(
                                        f"\nEnter misc option:\n"
                                        f"1: {Fore.GREEN}Remove Damage Effect{Style.RESET_ALL}\n"
                                        f"2: {Fore.GREEN}Anti Damage Affect{Style.RESET_ALL}\n"
                                        f"Type 'back' to return to the previous menu.\n: ",
                                        valid_values=[1, 2]
                                    )

                                    if damage_option == 'back':
                                        print(f"{Fore.CYAN}\nReturning to misc tweaks.{Style.RESET_ALL}")
                                        break

                                    match damage_option:
                                        case 1:
                                            addon = "a0542ee89ad3cc311bb3f7d23ef94fe4"
                                            addon2 = "5873cfba79134ecfec6658f559d8f320"
                                            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                                        case 2:
                                            addon = "a0542ee89ad3cc311bb3f7d23ef94fe4"
                                            addon2 = "614546fcea8e0411a1c94d669809a459"
                                            return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 4:
                                addon = "960b11e6e7d549c8b12044201025093f"
                                addon2 = "ac59980bedb36f4b240633b08b532d08"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 5:
                                addon = ["7b11fe3312b0801492d3e0f8dce62043", "853395973e94bf11a1c9edb8110da786", "1a566c1fd2deac2677bfa26b357b5cf9", "134d345ef675a18d2c73cdbb5ca03394", "f191e4a1f7ff200c57229c8c65c2e763", "18957c939764efa83229b65a05ab3fa7"]
                                addon2 = "5873cfba79134ecfec6658f559d8f320"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                case 12:
                    while True:
                        addon = "bee6d1f805ba64ac6e385658fc49447f"
                        start_key2 = "images"
                        return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                case 13:
                    while True:
                        hookey = get_valid_input(
                            f"\nEnter background tweak:\n"
                            f"1: {Fore.LIGHTMAGENTA_EX}Knuckles 2 perc{Style.RESET_ALL}\n"
                            f"2: {Fore.LIGHTMAGENTA_EX}Remove CQR grip{Style.RESET_ALL}\n"
                            f"3: {Fore.LIGHTMAGENTA_EX}Custom Thumbnails{Style.RESET_ALL}\n"
                            f"4: {Fore.LIGHTMAGENTA_EX}Remove aug a3 screws?{Style.RESET_ALL}\n"
                            f"Type 'back' to return to the previous menu.\n: ",
                            valid_values=[1, 2, 3, 4]
                        )

                        if hookey == 'back':
                            print(f"{Fore.CYAN}\nReturning to sight options.{Style.RESET_ALL}")
                            break

                        match hookey:
                            case 1:
                                addon = 'bf4a84852a2300227a8c7ecbc593d6d1'
                                addon2 = '76c8148ff29a29a8d46261b8a48db036'
                                push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                addon = 'bf51e6e8a19a4364734d36418f013808'
                                addon2 = '5873cfba79134ecfec6658f559d8f320'
                                push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                addon = "b87d3643e63269f553e020761986b0e3"
                                addon2 = "5873cfba79134ecfec6658f559d8f320"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 2:
                                addon = "14f489ef172a8899f571595c61013a91"
                                addon2 = "5873cfba79134ecfec6658f559d8f320"
                                push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                addon = "9d5d3ec6c7d9a466c888a9bd60cea222"
                                addon2 = "5873cfba79134ecfec6658f559d8f320"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 3:
                                addon = ["00b9f533f9739f829ecb4d72e60ec841", "0a725ed7927051ed526b31158e2ce213", "1b030ebbf2cc0eab987aa4f0fa3c474c", "2afd13a62c7c0b3b1c2f890c8df414e1","2b73028548ae918749458b685ba88f15","2dffeacf8620c37153f92fb2e93875f6","3d81d3d2a405b6acccca1a5ff522452b","04d64e18de34930fb909e48fe32df75c","8c4ecfd01667894ccc28729381b7c961","8d64b6f06a24207325eaabc141f7b54d","34b0f819cf882052aad094bf80419818","39be7295a9c334bef2ded9656cb6ab77","41e9daaa2a700a95f60f4fe5b45c493d","131c91aacb28dca4f974e6b4d09b2187","257c343da94c82cd4a7438e20b29c85c","341ca8b0c154765107bc2b9054084a64","749ae7b4720ea5e8e7ae60bcc472663e","2742d209d5efe28bb8df04b00a8f20d9","09922d6682b45ac0188c1828e0f1ffec","51734a6c5275eae053032a662731714f","856850c0c41bd27fdcb248b5d617b488","8200118ad2f288955fb23d5faa007e99","68473387faf44e63f33bd7b453b59df0","b43f35d506af6eda2f591d6adc2a2b22","b63c3c28554fd0fe57281c82c3d4f199","be0b884ad248efa2c54462ac5e337d49","c18d78a46d07eef94ea9154e4e4278b3","c195f31e03816e3d479cd2a43929b166","ccead3a1fae84a5273def0435e3b5903","de7413488e58f7d417811dc6eb41ee91","ee22325254317256288199c682b90ea6","f3dfd536b6cd589d07797f169119dfbd","fc85fdf2775dfd8b83f69e1ed014ce12"]
                                start_key2 = "images"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 4:
                                addon = ["5d57fd2bdabbe4721ff06d5166337b8e","5c0f06ef0a10bf4607d64ad86aed1158"]
                                addon2 = "5873cfba79134ecfec6658f559d8f320"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                case 14:
                    while True:
                        texture = get_valid_input(
                            f"\nMight make your game look ugly:\n"
                            f"1: {Fore.LIGHTMAGENTA_EX}Lean(Purple){Style.RESET_ALL}\n"
                            f"2: {Fore.LIGHTMAGENTA_EX}Lapis(Dark blue){Style.RESET_ALL}\n"
                            f"3: {Fore.LIGHTMAGENTA_EX}Low graphics type shi{Style.RESET_ALL}\n"
                            f"4: {Fore.LIGHTMAGENTA_EX}Black(kinda ass){Style.RESET_ALL}\n"
                            f"Type 'back' to return to the previous menu.\n: ",
                            valid_values=[1, 2, 3, 4]
                        )

                        if texture == 'back':
                            print(f"{Fore.CYAN}\nReturning to sight options.{Style.RESET_ALL}")
                            break

                        match texture:
                            case 1:
                                start_key = "texture1"
                                addon2 = "57ad28bdb099086401b2a9c7c0b766a9"
                                push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                start_key = "texture2"
                                addon2 = "291d1fb0301bca507b3724dec4165de8"
                                push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                start_key = "texture3"
                                addon2 = "9064c5e71824f58a79c233b9a8143974"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names

                            case 2:
                                start_key = "texture1"
                                addon2 = "e045b7c5fc23a85074263e78a2cf3cd2"
                                push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                start_key = "texture2"
                                addon2 = "38ccdc2b62345593d716ac39869d613e"
                                push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                start_key = "texture3"
                                addon2 = "0b1977a3636fe388f45c335b84316f32"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 3:
                                start_key = "texture1"
                                addon2 = "57ad28bdb099086401b2a9c7c0b766a9"
                                push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                start_key = "texture2"
                                addon2 = "291d1fb0301bca507b3724dec4165de8"
                                push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                start_key = "texture3"
                                addon2 = "57ad28bdb099086401b2a9c7c0b766a9"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names
                            case 4:
                                start_key = "texture1"
                                addon2 = "87040809250d70d1c56d43e9284bcc1a"
                                push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                start_key = "texture2"
                                addon2 = "87040809250d70d1c56d43e9284bcc1a"
                                push(json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names)
                                start_key = "texture3"
                                addon2 = "87040809250d70d1c56d43e9284bcc1a"
                                return json_data, start_key, start_key2, addon, addon2, skip, game_pre, display_names


        except Exception as e:
            print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")
