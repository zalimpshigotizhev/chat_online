from infra.repositories.messages import MemoryChatRepository, BaseChatRepository
from logic.commands.messages import CreateChatCommand, CreateChatCommandHandler
from logic.mediator import Mediator


def init_mediator(
    mediator: Mediator,
    chat_repository: BaseChatRepository,

) -> None:
    mediator.register_event(
        CreateChatCommand,
        [CreateChatCommandHandler(chat_repository=chat_repository)],
    )