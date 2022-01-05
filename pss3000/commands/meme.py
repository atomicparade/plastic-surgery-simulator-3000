"""Meme-related commands."""
import logging
import os
from pathlib import Path

import hikari
import tanjun

from pss3000.commands.common import CommandModuleInitialiser, StrOptions


class MemeInitialiser(CommandModuleInitialiser):
    """Initialiser for the meme module."""

    def __init__(self) -> None:
        try:
            os.makedirs(Path("assets", "meme", "templates-global"), exist_ok=True)
            self._initialised_successfully = True
            logging.info("Successfully initialised meme module")
        except PermissionError:
            logging.error("Unable to create directory assets/meme/templates-global/")

    def reload(self) -> None:
        pass


meme_initialiser = MemeInitialiser()

meme_commands = tanjun.slash_command_group(
    "meme",
    "Meme-related commands",
)

flip_options = StrOptions(
    "Do not flip",
    "Flip horizontally",
    "Flip vertically",
    "Flip both horizontally and vertically",
)

make_square_options = StrOptions(
    "Do not squish into a square",
    "Squish into a square",
)

invert_colours_options = StrOptions(
    "Do not invert colours",
    "Invert colours",
)

make_monochrome_options = StrOptions(
    "Do not make monochrome",
    "Make monochrome",
)

deep_fry_options = StrOptions(
    "Do not deep-fry",
    "Just a little",
    "That's a lot of oil",
    "Very burnt",
)

blur_options = StrOptions(
    "Do not blur",
    "Just a little",
    "Where are my glasses?",
    "Help",
)


@meme_commands.with_command
@tanjun.with_str_slash_option(
    "image_url_or_template_name",
    "The image URL or template name (use /meme template-list to see a list)",
)
@tanjun.with_str_slash_option(
    "flip",
    "Whether to flip the image (default = do not)",
    choices=list(flip_options),
    default=flip_options.default,
)
@tanjun.with_str_slash_option(
    "make_square",
    "Whether to squish the image into a square (default = do not)",
    choices=list(make_square_options),
    default=make_square_options.default,
)
@tanjun.with_str_slash_option(
    "invert_colours",
    "Whether to invert the image's colours (default = do not)",
    choices=list(invert_colours_options),
    default=invert_colours_options.default,
)
@tanjun.with_str_slash_option(
    "make_monochrome",
    "Whether to turn the image black-and-white (default = do not)",
    choices=list(make_monochrome_options),
    default=make_monochrome_options.default,
)
@tanjun.with_int_slash_option(
    "rotate",
    "Number of degrees to rotate the image clockwise (default = 0/do not rotate)",
    default=0,
)
@tanjun.with_str_slash_option(
    "deep_fry",
    "How much to deep-fry the image",
    choices=list(deep_fry_options),
    default=deep_fry_options.default,
)
@tanjun.with_str_slash_option(
    "blur",
    "How much to blur the image (0 to 100; default = 0/do not blur)",
    choices=list(blur_options),
    default=blur_options.default,
)
@tanjun.as_slash_command(
    "create",
    "Create a meme",
    default_to_ephemeral=False,
)
# pylint: disable-next=too-many-arguments
# pylint: disable-next=too-many-branches
async def command_meme_create(
    ctx: tanjun.abc.SlashContext,
    image_url_or_template_name: str,
    flip: str,
    make_square: str,
    invert_colours: str,
    make_monochrome: str,
    rotate: int,
    deep_fry: str,
    blur: str,
) -> None:
    """Create a meme."""
    meme_command = f"create_meme({image_url_or_template_name})"

    if flip == flip_options.flip_horizontally:
        meme_command = f"{meme_command} +flip_horizontally"
    elif flip == flip_options.flip_vertically:
        meme_command = f"{meme_command} +flip_vertically"
    elif flip == flip_options.flip_both_horizontally_and_vertically:
        meme_command = f"{meme_command} +flip_both_horizontally_and_vertically"

    if make_square == make_square_options.squish_into_a_square:
        meme_command = f"{meme_command} +squish_into_a_square"

    if invert_colours == invert_colours_options.invert_colours:
        meme_command = f"{meme_command} +invert_colours"

    if make_monochrome == make_monochrome_options.make_monochrome:
        meme_command = f"{meme_command} +make_monochrome"

    if rotate != 0:
        meme_command = f"{meme_command} +rotate({rotate})"

    if deep_fry == deep_fry_options.just_a_little:
        meme_command = f"{meme_command} +deep_fry.just_a_little"
    elif deep_fry == deep_fry_options.thats_a_lot_of_oil:
        meme_command = f"{meme_command} +deep_fry.thats_a_lot_of_oil"
    elif deep_fry == deep_fry_options.very_burnt:
        meme_command = f"{meme_command} +deep_fry.very_burnt"

    if blur == blur_options.just_a_little:
        meme_command = f"{meme_command} +blur.just_a_little"
    elif blur == blur_options.where_are_my_glasses:
        meme_command = f"{meme_command} +blur.where_are_my_glasses"
    elif blur == blur_options.help:
        meme_command = f"{meme_command} +blur.help"

    try:
        await ctx.respond(meme_command)
    except (hikari.ForbiddenError, hikari.NotFoundError):
        pass


@meme_commands.with_command
@tanjun.with_str_slash_option(
    "template_name",
    "The name of the template (must be unique)",
)
@tanjun.with_str_slash_option(
    "image_url",
    "The image URL",
)
@tanjun.as_slash_command(
    "template-add",
    "Add a meme template",
    default_to_ephemeral=False,
)
async def command_meme_template_add(
    ctx: tanjun.abc.SlashContext,
    template_name: str,
    image_url: str,
) -> None:
    """Add a meme template."""
    try:
        await ctx.respond(f"Adding meme template {template_name} for URL {image_url}")
    except (hikari.ForbiddenError, hikari.NotFoundError):
        pass


@meme_commands.with_command
@tanjun.with_str_slash_option(
    "template_name",
    "The name of the template",
)
@tanjun.as_slash_command(
    "template-delete",
    "Delete a meme template",
    default_to_ephemeral=False,
)
async def command_meme_template_delete(
    ctx: tanjun.abc.SlashContext,
    template_name: str,
) -> None:
    """Delete a meme template."""
    try:
        await ctx.respond(f"Deleting meme template {template_name}")
    except (hikari.ForbiddenError, hikari.NotFoundError):
        pass


@meme_commands.with_command
@tanjun.as_slash_command(
    "template-list",
    "Show the list of meme templates",
    default_to_ephemeral=True,
)
async def command_meme_template_list(
    ctx: tanjun.abc.SlashContext,
) -> None:
    """Show the list of meme templates."""
    try:
        await ctx.respond("List of meme templates")
    except (hikari.ForbiddenError, hikari.NotFoundError):
        pass


component = tanjun.Component().add_slash_command(meme_commands)
slash_loader = component.make_loader()
command_module_initialiser = meme_initialiser
