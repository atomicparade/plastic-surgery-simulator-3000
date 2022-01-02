"""Miscellaneous bot commands."""
import hikari
import tanjun

component = tanjun.Component()


@component.with_slash_command
@tanjun.as_slash_command(
    "about",
    "Get information about Plastic Surgery Simulator 3000",
    default_to_ephemeral=True,
)
async def command_about(
    ctx: tanjun.abc.SlashContext,
) -> None:
    """Respond with information about the bot."""
    embed = hikari.Embed(
        title="About Plastic Surgery Simulator 3000",
        description=(
            "Want to see what your friends would like with Obama's face? "
            "I can help!\n"
            "\n"
            "Want to ban a word? I can help with that, too!\n"
            "\n"
            "Want to put something in a jar? I won't ask any questions!"
        ),
    )

    try:
        await ctx.respond(embed=embed)
    except (hikari.ForbiddenError, hikari.NotFoundError):
        pass


slash_loader = component.make_loader()
