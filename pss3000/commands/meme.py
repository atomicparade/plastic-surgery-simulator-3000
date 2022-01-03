"""Meme-related commands."""
import hikari
import tanjun

meme_commands = tanjun.slash_command_group(
    "meme",
    "Meme-related commands",
)

# TODO: Make str slash options enums?


@meme_commands.with_command
@tanjun.with_str_slash_option(
    "image_url_or_template_name",
    "The image URL or template name (use /meme template-list to see a list)",
)
@tanjun.with_str_slash_option(
    "flip",
    "Whether to flip the image (default = do not)",
    choices=[
        "Do not flip",
        "Flip horizontally",
        "Flip vertically",
        "Flip both horizontally and vertically",
    ],
    default="Do not flip",
)
@tanjun.with_str_slash_option(
    "make_square",
    "Whether to squish the image into a square (default = do not)",
    choices=[
        "Do not squish into a square",
        "Squish into a square",
    ],
    default="Do not squish into a square",
)
@tanjun.with_str_slash_option(
    "invert_colours",
    "Whether to invert the image's colours (default = do not)",
    choices=[
        "Do not invert colours",
        "Invert colours",
    ],
    default="Do not invert colours",
)
@tanjun.with_str_slash_option(
    "make_monochrome",
    "Whether to turn the image black-and-white (default = do not)",
    choices=[
        "Do not make monochrome",
        "Make monochrome",
    ],
    default="Do not make monochrome",
)
@tanjun.with_int_slash_option(
    "rotate",
    "Number of degrees to rotate the image clockwise (default = 0/do not rotate)",
    default=0,
)
@tanjun.with_str_slash_option(
    "deep_fry",
    "How much to deep-fry the image",
    choices=[
        "Do not deep-fry",
        "Just a little",
        "That's a lot of oil",
        "Very burnt",
    ],
    default="Do not deep-fry",
)
@tanjun.with_str_slash_option(
    "blur",
    "How much to blur the image (0 to 100; default = 0/do not blur)",
    choices=[
        "Do not blur",
        "Just a little",
        "Where are my glasses?",
        "Help",
    ],
    default="Do not blur",
)
@tanjun.as_slash_command(
    "create",
    "Create a meme",
    default_to_ephemeral=False,
)
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
    try:
        await ctx.respond("meme")
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
