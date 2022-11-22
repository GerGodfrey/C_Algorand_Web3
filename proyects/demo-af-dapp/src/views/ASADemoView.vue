<template>
    <div id="sendalgo-app">
        <h3>Select wallet</h3>
        <div class="d-grid gap-2 mb-5">
            <button @click="connectToAlgoSigner('Localhost')" class="btn btn-primary">
                AlgoSigner (Localhost)
            </button>
        </div>
        <div v-if="this.sender !== ''" class="mb-5">
            <h3>Connected</h3>
            <p>
                Connection: <span>{{ this.connection }}</span>
            </p>
            <p>
                Network: <span>{{ this.network }}</span>
            </p>
            <p>
                Account: <span>{{ this.sender }}</span>
            </p>
        </div>
        <send-asset-form
            v-if="this.connection === 'algosigner' && this.network === 'Localhost'"
            :connection="this.connection"
            :network="this.network"
            :receiver="this.sender"
        />
    </div>
</template>

<script>
export default {
    data() {
        return {
            connection: "", // myalgo | walletconnect | algosigner
            connector: null, // wallet connector obj
            network: "", // Localhost | TestNet
            sender: "", // connected account
            receiver: "",
        };
    },
    methods: {
        async connectToAlgoSigner(network) {
            this.network = network;
            const AlgoSigner = window.AlgoSigner;

            if (typeof AlgoSigner !== "undefined") {
                await AlgoSigner.connect();
                const accounts = await AlgoSigner.accounts({
                    ledger: this.network,
                });

                if (this.network === "Localhost") {
                    // use non-creator address
                    this.sender = accounts[1].address;
                } else {
                    this.sender = accounts[0].address;
                    this.receiver = accounts[1].address;
                }

                this.connection = "algosigner";
            }
        },
    },
};
</script>
