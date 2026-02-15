import {
  Button as SdsButton,
  Checkbox as SdsCheckbox,
  Input as SdsInput,
  Switch as SdsSwitch,
  Text as SdsText
} from "../components";
import "./GameWebshopCatalogPage.css";

const gameCards = [
  {
    title: "Galactic Raiders",
    genre: "Action RPG",
    platform: "PC / PS5",
    price: "$39.99",
    discount: "-20%"
  },
  {
    title: "Kingdoms of Ash",
    genre: "Strategy",
    platform: "PC / Xbox",
    price: "$29.99",
    discount: "-15%"
  },
  {
    title: "Neon Drift X",
    genre: "Racing",
    platform: "PC / Switch",
    price: "$24.99",
    discount: "-10%"
  },
  {
    title: "Mythic Tactics",
    genre: "Turn-based",
    platform: "PC / Mobile",
    price: "$19.99",
    discount: "-30%"
  },
  {
    title: "Starforge Online",
    genre: "MMO",
    platform: "PC",
    price: "$49.99",
    discount: "New"
  },
  {
    title: "Depth Signal",
    genre: "Horror",
    platform: "PC / PS5",
    price: "$34.99",
    discount: "-25%"
  }
];

export function GameWebshopCatalogPage() {
  return (
    <div className="sds-game-catalog">
      <header className="sds-game-catalog__header">
        <div className="sds-game-catalog__container sds-game-catalog__header-row">
          <SdsText variant="heading" as="p">
            Pixel Forge Store
          </SdsText>
          <nav className="sds-game-catalog__header-nav" aria-label="Primary">
            <SdsButton variant="subtle" size="small">
              New Releases
            </SdsButton>
            <SdsButton variant="subtle" size="small">
              Top Sellers
            </SdsButton>
            <SdsButton variant="subtle" size="small">
              Genres
            </SdsButton>
          </nav>
          <div className="sds-game-catalog__header-actions">
            <SdsButton variant="neutral" size="small">
              Sign in
            </SdsButton>
            <SdsButton size="small">Cart (2)</SdsButton>
          </div>
        </div>
        <div className="sds-game-catalog__container sds-game-catalog__mobile-header">
          <SdsText variant="heading" as="p">
            Pixel Forge Store
          </SdsText>
          <SdsButton variant="neutral" size="small">
            Menu
          </SdsButton>
        </div>
        <div className="sds-game-catalog__container sds-game-catalog__mobile-menu-open">
          <SdsButton variant="subtle" size="small">
            New Releases
          </SdsButton>
          <SdsButton variant="subtle" size="small">
            Top Sellers
          </SdsButton>
          <SdsButton variant="subtle" size="small">
            Genres
          </SdsButton>
        </div>
      </header>

      <main>
        <section className="sds-game-catalog__hero">
          <div className="sds-game-catalog__container sds-game-catalog__hero-inner">
            <SdsText variant="titlePage">Game Catalog</SdsText>
            <SdsText variant="body" className="sds-game-catalog__hero-copy">
              Discover new worlds, compare editions, and build your next playlist of games for
              weekend raids.
            </SdsText>
            <div className="sds-game-catalog__hero-actions">
              <SdsButton>Browse all deals</SdsButton>
              <SdsButton variant="neutral">Wishlist</SdsButton>
            </div>
          </div>
        </section>

        <section className="sds-game-catalog__results">
          <div className="sds-game-catalog__container">
            <div className="sds-game-catalog__content-grid">
              <aside className="sds-game-catalog__filters" aria-label="Catalog filters">
                <SdsText variant="subheading" as="h2">
                  Filters
                </SdsText>
                <SdsInput label="Search title" placeholder="Type game name" />
                <div className="sds-game-catalog__filter-group">
                  <SdsText variant="strong">Platforms</SdsText>
                  <SdsCheckbox label="PC" valueType="checked" />
                  <SdsCheckbox label="PlayStation" />
                  <SdsCheckbox label="Xbox" />
                  <SdsCheckbox label="Switch" />
                </div>
                <div className="sds-game-catalog__filter-group">
                  <SdsText variant="strong">Preferences</SdsText>
                  <SdsSwitch label="Only discounted" valueType="checked" />
                  <SdsSwitch label="Co-op enabled" />
                </div>
                <SdsButton variant="neutral">Reset filters</SdsButton>
              </aside>

              <div className="sds-game-catalog__cards-section">
                <div className="sds-game-catalog__cards-head">
                  <SdsText variant="subtitle" as="h2">
                    Featured titles
                  </SdsText>
                  <SdsText variant="small">Showing 6 of 126 games</SdsText>
                </div>
                <div className="sds-game-catalog__cards-grid">
                  {gameCards.map((game) => (
                    <article className="sds-game-catalog__card" key={game.title}>
                      <div className="sds-game-catalog__cover" aria-hidden />
                      <div className="sds-game-catalog__card-body">
                        <SdsText variant="heading" as="h3">
                          {game.title}
                        </SdsText>
                        <SdsText variant="small">
                          {game.genre} - {game.platform}
                        </SdsText>
                        <div className="sds-game-catalog__card-meta">
                          <SdsText variant="strong">{game.price}</SdsText>
                          <SdsText variant="small" className="sds-game-catalog__badge">
                            {game.discount}
                          </SdsText>
                        </div>
                        <SdsButton size="small">Add to cart</SdsButton>
                      </div>
                    </article>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>

      <footer className="sds-game-catalog__footer">
        <div className="sds-game-catalog__container sds-game-catalog__footer-inner">
          <SdsText variant="small">Pixel Forge Store</SdsText>
          <SdsText variant="small">Secure checkout and instant key delivery.</SdsText>
        </div>
      </footer>
    </div>
  );
}
