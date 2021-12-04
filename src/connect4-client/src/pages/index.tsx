import type { NextPage } from "next";
import { App } from "../components";
import { GameApiClient } from "../external_services/game_api_client";
import getConfig from 'next/config'

type Props = {
  API_URL: string
}
const Home = ({ API_URL }: Props) => {
  return <App columns={7} rows={6} client={new GameApiClient(API_URL)} />;
};

export const getServerSideProps = async () => {
  const { serverRuntimeConfig } = getConfig()
  const API_URL = serverRuntimeConfig.API_URL

  console.assert(API_URL, "We might need this environment variable to work")
  console.log("API_URL: " + API_URL)

  return {
    props: {
      API_URL
    }
  }
}

export default Home;
